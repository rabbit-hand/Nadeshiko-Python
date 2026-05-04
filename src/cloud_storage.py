"""
Cloud Storage System - World-changing project synchronization and sharing
"""

import os
import json
import hashlib
import asyncio
import aiohttp
import aiofiles
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
import zipfile
import shutil
from pathlib import Path

@dataclass
class CloudProject:
    id: str
    name: str
    description: str
    author: str
    created_at: datetime
    updated_at: datetime
    tags: List[str]
    is_public: bool
    file_count: int
    size: int
    collaborators: List[str]

@dataclass
class SyncOperation:
    type: str  # 'upload', 'download', 'delete', 'sync'
    file_path: str
    timestamp: datetime
    checksum: str
    status: str  # 'pending', 'in_progress', 'completed', 'failed'

class CloudStorage:
    """Revolutionary cloud storage system"""
    
    def __init__(self, api_key: str, endpoint: str = "https://api.nadesiko.cloud"):
        self.api_key = api_key
        self.endpoint = endpoint
        self.local_cache = {}
        self.sync_queue = []
        self.sync_in_progress = False
        
    async def authenticate(self) -> bool:
        """Authenticate with cloud service"""
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.endpoint}/auth",
                json={"api_key": self.api_key}
            ) as response:
                return response.status == 200
    
    async def upload_project(self, project_path: str, project_name: str, 
                          description: str = "", tags: List[str] = None, 
                          is_public: bool = False) -> CloudProject:
        """Upload entire project to cloud"""
        if tags is None:
            tags = []
        
        # Create project metadata
        project_id = self._generate_project_id(project_name)
        
        # Calculate project info
        total_size = 0
        file_count = 0
        
        for root, dirs, files in os.walk(project_path):
            for file in files:
                file_path = os.path.join(root, file)
                if not file.startswith('.') and not file.endswith('.pyc'):
                    total_size += os.path.getsize(file_path)
                    file_count += 1
        
        project = CloudProject(
            id=project_id,
            name=project_name,
            description=description,
            author="User",  # Would get from auth
            created_at=datetime.now(),
            updated_at=datetime.now(),
            tags=tags,
            is_public=is_public,
            file_count=file_count,
            size=total_size,
            collaborators=[]
        )
        
        # Create project archive
        archive_path = self._create_project_archive(project_path, project_id)
        
        # Upload to cloud
        async with aiohttp.ClientSession() as session:
            with open(archive_path, 'rb') as f:
                data = aiohttp.FormData()
                data.add_field('project', json.dumps(asdict(project), 'application/json')
                data.add_field('archive', f, f'{project_id}.zip', 'application/zip')
                
                async with session.post(
                    f"{self.endpoint}/projects/upload",
                    data=data,
                    headers={"Authorization": f"Bearer {self.api_key}"}
                ) as response:
                    if response.status == 201:
                        result = await response.json()
                        os.remove(archive_path)
                        return CloudProject(**result['project'])
        
        raise Exception("Failed to upload project")
    
    async def download_project(self, project_id: str, download_path: str) -> bool:
        """Download project from cloud"""
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.endpoint}/projects/{project_id}/download",
                headers={"Authorization": f"Bearer {self.api_key}"}
            ) as response:
                if response.status == 200:
                    # Download archive
                    archive_path = os.path.join(download_path, f"{project_id}.zip")
                    
                    async with aiofiles.open(archive_path, 'wb') as f:
                        async for chunk in response.content.iter_chunked(8192):
                            await f.write(chunk)
                    
                    # Extract archive
                    self._extract_project_archive(archive_path, download_path)
                    os.remove(archive_path)
                    
                    return True
        
        return False
    
    async def list_projects(self, tags: List[str] = None, 
                         search: str = None, 
                         author: str = None) -> List[CloudProject]:
        """List available projects"""
        params = {}
        if tags:
            params['tags'] = ','.join(tags)
        if search:
            params['search'] = search
        if author:
            params['author'] = author
        
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.endpoint}/projects",
                params=params,
                headers={"Authorization": f"Bearer {self.api_key}"}
            ) as response:
                if response.status == 200:
                    result = await response.json()
                    return [CloudProject(**p) for p in result['projects']]
        
        return []
    
    async def sync_project(self, local_path: str, project_id: str) -> List[SyncOperation]:
        """Synchronize project with cloud version"""
        # Get local file checksums
        local_files = self._get_local_files(local_path)
        
        # Get remote file info
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.endpoint}/projects/{project_id}/files",
                headers={"Authorization": f"Bearer {self.api_key}"}
            ) as response:
                if response.status == 200:
                    remote_files = await response.json()
                else:
                    remote_files = []
        
        # Determine sync operations
        operations = []
        
        for file_path, checksum in local_files.items():
            relative_path = os.path.relpath(file_path, local_path)
            
            if relative_path not in remote_files:
                # New file - upload
                operations.append(SyncOperation(
                    type='upload',
                    file_path=relative_path,
                    timestamp=datetime.now(),
                    checksum=checksum,
                    status='pending'
                ))
            elif remote_files[relative_path] != checksum:
                # Modified file - upload
                operations.append(SyncOperation(
                    type='upload',
                    file_path=relative_path,
                    timestamp=datetime.now(),
                    checksum=checksum,
                    status='pending'
                ))
        
        for file_path, checksum in remote_files.items():
            full_path = os.path.join(local_path, file_path)
            
            if file_path not in local_files:
                # Deleted file - delete locally
                operations.append(SyncOperation(
                    type='delete',
                    file_path=file_path,
                    timestamp=datetime.now(),
                    checksum=checksum,
                    status='pending'
                ))
        
        # Execute sync operations
        results = []
        for operation in operations:
            try:
                operation.status = 'in_progress'
                
                if operation.type == 'upload':
                    await self._upload_file(local_path, operation.file_path, project_id)
                elif operation.type == 'delete':
                    if os.path.exists(os.path.join(local_path, operation.file_path)):
                        os.remove(os.path.join(local_path, operation.file_path))
                
                operation.status = 'completed'
                
            except Exception as e:
                operation.status = 'failed'
                print(f"Sync failed for {operation.file_path}: {e}")
            
            results.append(operation)
        
        return results
    
    async def share_project(self, project_id: str, users: List[str], 
                          permissions: str = 'read') -> bool:
        """Share project with other users"""
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.endpoint}/projects/{project_id}/share",
                json={
                    "users": users,
                    "permissions": permissions
                },
                headers={"Authorization": f"Bearer {self.api_key}"}
            ) as response:
                return response.status == 200
    
    async def get_project_activity(self, project_id: str, 
                               since: datetime = None) -> List[Dict]:
        """Get project activity log"""
        params = {}
        if since:
            params['since'] = since.isoformat()
        
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.endpoint}/projects/{project_id}/activity",
                params=params,
                headers={"Authorization": f"Bearer {self.api_key}"}
            ) as response:
                if response.status == 200:
                    return await response.json()
        
        return []
    
    def _generate_project_id(self, project_name: str) -> str:
        """Generate unique project ID"""
        timestamp = datetime.now().isoformat()
        content = f"{project_name}_{timestamp}"
        return hashlib.sha256(content.encode()).hexdigest()[:16]
    
    def _create_project_archive(self, project_path: str, project_id: str) -> str:
        """Create zip archive of project"""
        archive_path = f"/tmp/{project_id}.zip"
        
        with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(project_path):
                for file in files:
                    if not file.startswith('.') and not file.endswith('.pyc'):
                        file_path = os.path.join(root, file)
                        arc_path = os.path.relpath(file_path, project_path)
                        zipf.write(file_path, arc_path)
        
        return archive_path
    
    def _extract_project_archive(self, archive_path: str, extract_path: str):
        """Extract project archive"""
        with zipfile.ZipFile(archive_path, 'r') as zipf:
            zipf.extractall(extract_path)
    
    def _get_local_files(self, path: str) -> Dict[str, str]:
        """Get all local files with checksums"""
        files = {}
        
        for root, dirs, filenames in os.walk(path):
            for filename in filenames:
                if not filename.startswith('.') and not filename.endswith('.pyc'):
                    file_path = os.path.join(root, filename)
                    relative_path = os.path.relpath(file_path, path)
                    
                    with open(file_path, 'rb') as f:
                        checksum = hashlib.sha256(f.read()).hexdigest()
                        files[relative_path] = checksum
        
        return files
    
    async def _upload_file(self, project_path: str, file_path: str, project_id: str):
        """Upload individual file"""
        full_path = os.path.join(project_path, file_path)
        
        async with aiohttp.ClientSession() as session:
            with open(full_path, 'rb') as f:
                data = aiohttp.FormData()
                data.add_field('file', f, file_path, 'application/octet-stream')
                data.add_field('path', file_path)
                
                async with session.post(
                    f"{self.endpoint}/projects/{project_id}/files",
                    data=data,
                    headers={"Authorization": f"Bearer {self.api_key}"}
                ) as response:
                    if response.status != 200:
                        raise Exception(f"Upload failed: {response.status}")

class CloudSyncManager:
    """Automatic cloud synchronization manager"""
    
    def __init__(self, storage: CloudStorage, project_path: str, project_id: str):
        self.storage = storage
        self.project_path = project_path
        self.project_id = project_id
        self.sync_interval = 30  # seconds
        self.running = False
        
    async def start_auto_sync(self):
        """Start automatic synchronization"""
        self.running = True
        
        while self.running:
            try:
                operations = await self.storage.sync_project(
                    self.project_path, self.project_id
                )
                
                # Log sync results
                completed = sum(1 for op in operations if op.status == 'completed')
                failed = sum(1 for op in operations if op.status == 'failed')
                
                if completed > 0 or failed > 0:
                    print(f"Sync completed: {completed} files, {failed} failed")
                
            except Exception as e:
                print(f"Auto-sync error: {e}")
            
            await asyncio.sleep(self.sync_interval)
    
    def stop_auto_sync(self):
        """Stop automatic synchronization"""
        self.running = False

# Usage example
async def main():
    # Initialize cloud storage
    storage = CloudStorage(api_key="your-api-key")
    
    # Authenticate
    if await storage.authenticate():
        print("Authenticated successfully")
        
        # Upload project
        project = await storage.upload_project(
            project_path="./my_nadesiko_project",
            project_name="My Awesome Project",
            description="A revolutionary Nadesiko Python project",
            tags=["education", "ai", "visual"],
            is_public=True
        )
        
        print(f"Project uploaded: {project.id}")
        
        # Start auto-sync
        sync_manager = CloudSyncManager(storage, "./my_nadesiko_project", project.id)
        sync_task = asyncio.create_task(sync_manager.start_auto_sync())
        
        # Keep running
        await sync_task

if __name__ == "__main__":
    asyncio.run(main())
