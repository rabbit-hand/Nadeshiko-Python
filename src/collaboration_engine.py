"""
Real-time Collaboration Engine - World-changing collaborative programming
"""

import asyncio
import websockets
import json
import uuid
from typing import Dict, List, Set, Any
from dataclasses import dataclass, asdict
from datetime import datetime
import threading
import queue

@dataclass
class User:
    id: str
    name: str
    cursor_position: tuple
    color: str
    is_online: bool = True

@dataclass
class Operation:
    id: str
    user_id: str
    type: str  # 'insert', 'delete', 'cursor_move', 'block_add', 'block_move'
    position: tuple
    content: Any
    timestamp: datetime

class CollaborationServer:
    """Real-time collaboration server"""
    
    def __init__(self, host="localhost", port=8765):
        self.host = host
        self.port = port
        self.users: Dict[str, User] = {}
        self.operations: List[Operation] = []
        self.document_content = ""
        self.visual_blocks = {}
        
    async def register_user(self, websocket, user_data):
        """Register new user"""
        user_id = str(uuid.uuid4())
        user = User(
            id=user_id,
            name=user_data.get('name', f'User_{user_id[:8]}'),
            cursor_position=(0, 0),
            color=self._generate_color(),
            is_online=True
        )
        
        self.users[user_id] = user
        
        # Send user registration confirmation
        await websocket.send(json.dumps({
            'type': 'user_registered',
            'user': asdict(user)
        }))
        
        # Broadcast user joined
        await self.broadcast({
            'type': 'user_joined',
            'user': asdict(user)
        }, exclude_websocket=websocket)
        
        # Send current document state
        await websocket.send(json.dumps({
            'type': 'document_state',
            'content': self.document_content,
            'blocks': self.visual_blocks,
            'users': [asdict(u) for u in self.users.values() if u.id != user_id]
        }))
        
        return user_id
    
    async def handle_operation(self, websocket, user_id, operation_data):
        """Handle user operation"""
        operation = Operation(
            id=str(uuid.uuid4()),
            user_id=user_id,
            type=operation_data['type'],
            position=operation_data.get('position', (0, 0)),
            content=operation_data.get('content', ''),
            timestamp=datetime.now()
        )
        
        self.operations.append(operation)
        
        # Apply operation to document
        if operation.type == 'insert':
            self.document_content = (
                self.document_content[:operation.position[0]] +
                operation.content +
                self.document_content[operation.position[0]:]
            )
        elif operation.type == 'delete':
            start, end = operation.position
            self.document_content = (
                self.document_content[:start] +
                self.document_content[end:]
            )
        elif operation.type == 'block_add':
            self.visual_blocks[operation.content['id']] = operation.content
        elif operation.type == 'block_move':
            block_id = operation.content['id']
            if block_id in self.visual_blocks:
                self.visual_blocks[block_id].update(operation.content)
        elif operation.type == 'cursor_move':
            if user_id in self.users:
                self.users[user_id].cursor_position = operation.position
        
        # Broadcast operation to all users
        await self.broadcast({
            'type': 'operation',
            'operation': asdict(operation),
            'user': asdict(self.users[user_id]) if user_id in self.users else None
        })
    
    async def broadcast(self, message: dict, exclude_websocket=None):
        """Broadcast message to all connected users"""
        if self.clients:
            message_str = json.dumps(message, default=str)
            disconnected = []
            
            for client, user_id in self.clients:
                if client != exclude_websocket:
                    try:
                        await client.send(message_str)
                    except websockets.exceptions.ConnectionClosed:
                        disconnected.append((client, user_id))
            
            # Remove disconnected clients
            for client, user_id in disconnected:
                await self.handle_disconnect(client, user_id)
    
    async def handle_disconnect(self, websocket, user_id):
        """Handle user disconnection"""
        if user_id in self.users:
            self.users[user_id].is_online = False
            
            await self.broadcast({
                'type': 'user_left',
                'user': asdict(self.users[user_id])
            })
            
            del self.users[user_id]
    
    def _generate_color(self):
        """Generate random color for user"""
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']
        import random
        return random.choice(colors)
    
    async def start_server(self):
        """Start the collaboration server"""
        self.clients = []
        
        async def handle_client(websocket, path):
            user_id = None
            
            try:
                async for message in websocket:
                    data = json.loads(message)
                    
                    if data['type'] == 'register':
                        user_id = await self.register_user(websocket, data)
                        self.clients.append((websocket, user_id))
                    
                    elif data['type'] == 'operation' and user_id:
                        await self.handle_operation(websocket, user_id, data)
                        
            except websockets.exceptions.ConnectionClosed:
                if user_id:
                    await self.handle_disconnect(websocket, user_id)
            finally:
                if websocket in [client for client, _ in self.clients]:
                    self.clients = [(c, uid) for c, uid in self.clients if c != websocket]
        
        self.server = await websockets.serve(handle_client, self.host, self.port)
        print(f"Collaboration server started on ws://{self.host}:{self.port}")
        
        await self.server.wait_closed()

class CollaborationClient:
    """Real-time collaboration client"""
    
    def __init__(self, name="Anonymous"):
        self.name = name
        self.websocket = None
        self.user_id = None
        self.callbacks = {}
        
    async def connect(self, server_url="ws://localhost:8765"):
        """Connect to collaboration server"""
        self.websocket = await websockets.connect(server_url)
        
        # Register user
        await self.websocket.send(json.dumps({
            'type': 'register',
            'name': self.name
        }))
        
        # Start listening for messages
        asyncio.create_task(self.listen())
    
    async def listen(self):
        """Listen for server messages"""
        async for message in self.websocket:
            data = json.loads(message)
            
            if data['type'] == 'user_registered':
                self.user_id = data['user']['id']
                self._trigger_callback('user_registered', data['user'])
            
            elif data['type'] == 'user_joined':
                self._trigger_callback('user_joined', data['user'])
            
            elif data['type'] == 'user_left':
                self._trigger_callback('user_left', data['user'])
            
            elif data['type'] == 'operation':
                self._trigger_callback('operation', data['operation'], data['user'])
            
            elif data['type'] == 'document_state':
                self._trigger_callback('document_state', data)
    
    async def send_operation(self, operation_type, content, position=(0, 0)):
        """Send operation to server"""
        if self.websocket:
            await self.websocket.send(json.dumps({
                'type': 'operation',
                'operation': {
                    'type': operation_type,
                    'content': content,
                    'position': position
                }
            }))
    
    def on(self, event_type, callback):
        """Register event callback"""
        self.callbacks[event_type] = callback
    
    def _trigger_callback(self, event_type, *args):
        """Trigger event callback"""
        if event_type in self.callbacks:
            self.callbacks[event_type](*args)

# Usage example
async def main():
    # Start server
    server = CollaborationServer()
    server_task = asyncio.create_task(server.start_server())
    
    # Connect client
    client = CollaborationClient("Test User")
    
    def on_operation(operation, user):
        print(f"Operation from {user['name']}: {operation['type']}")
    
    client.on('operation', on_operation)
    
    await client.connect()
    
    # Keep running
    await server_task

if __name__ == "__main__":
    asyncio.run(main())
