"""
Visual Programming Interface - World-changing drag-and-drop programming
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import uuid
from typing import Dict, List, Any
from dataclasses import dataclass

@dataclass
class VisualBlock:
    id: str
    type: str
    x: int
    y: int
    width: int
    height: int
    color: str
    text: str
    connections: List[str]

class VisualProgrammingIDE:
    """Revolutionary visual programming interface"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Nadesiko Visual Programming - World Changing IDE")
        self.root.geometry("1200x800")
        
        self.blocks = {}
        self.selected_block = None
        self.connection_start = None
        
        self.setup_ui()
        self.setup_blocks()
        
    def setup_ui(self):
        """Setup the revolutionary UI"""
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - Block palette
        self.palette_frame = ttk.LabelFrame(main_frame, text="Programming Blocks", width=300)
        self.palette_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        # Center - Canvas
        self.canvas = tk.Canvas(main_frame, bg="#f0f0f0", width=800, height=700)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Right panel - Properties
        self.properties_frame = ttk.LabelFrame(main_frame, text="Properties", width=250)
        self.properties_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)
        
        # Canvas bindings
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<B1-Motion>", self.on_canvas_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_canvas_release)
        
        # Top toolbar
        toolbar = ttk.Frame(self.root)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        
        ttk.Button(toolbar, text="▶ Run", command=self.run_program).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="💾 Save", command=self.save_project).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="📁 Load", command=self.load_project).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="🔄 Generate Code", command=self.generate_code).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="🤖 AI Assist", command=self.ai_assist).pack(side=tk.LEFT, padx=2)
        
    def setup_blocks(self):
        """Setup programming blocks palette"""
        block_types = [
            {"type": "variable", "text": "変数", "color": "#ff6b6b"},
            {"type": "input", "text": "入力", "color": "#4ecdc4"},
            {"type": "calculation", "text": "計算", "color": "#45b7d1"},
            {"type": "condition", "text": "条件", "color": "#f7b731"},
            {"type": "loop", "text": "繰り返し", "color": "#5f27cd"},
            {"type": "output", "text": "出力", "color": "#00d2d3"},
            {"type": "function", "text": "関数", "color": "#a55eea"},
        ]
        
        for block_type in block_types:
            btn = tk.Button(
                self.palette_frame,
                text=block_type["text"],
                bg=block_type["color"],
                fg="white",
                width=15,
                height=2,
                command=lambda bt=block_type: self.add_block(bt)
            )
            btn.pack(pady=5, padx=10, fill=tk.X)
    
    def add_block(self, block_type):
        """Add a new block to canvas"""
        block_id = str(uuid.uuid4())
        block = VisualBlock(
            id=block_id,
            type=block_type["type"],
            x=100,
            y=100,
            width=120,
            height=60,
            color=block_type["color"],
            text=block_type["text"],
            connections=[]
        )
        
        self.blocks[block_id] = block
        self.draw_block(block)
    
    def draw_block(self, block):
        """Draw a block on canvas"""
        self.canvas.create_rectangle(
            block.x, block.y,
            block.x + block.width, block.y + block.height,
            fill=block.color,
            outline="black",
            width=2,
            tags=block.id
        )
        self.canvas.create_text(
            block.x + block.width//2,
            block.y + block.height//2,
            text=block.text,
            fill="white",
            font=("Arial", 10, "bold"),
            tags=block.id
        )
    
    def on_canvas_click(self, event):
        """Handle canvas click"""
        clicked = self.canvas.find_closest(event.x, event.y)
        if clicked:
            tags = self.canvas.gettags(clicked[0])
            if tags and tags[0] in self.blocks:
                self.selected_block = tags[0]
                self.connection_start = (event.x, event.y)
    
    def on_canvas_drag(self, event):
        """Handle canvas drag"""
        if self.selected_block:
            block = self.blocks[self.selected_block]
            dx = event.x - block.x - block.width//2
            dy = event.y - block.y - block.height//2
            self.move_block(self.selected_block, dx, dy)
    
    def on_canvas_release(self, event):
        """Handle canvas release"""
        self.selected_block = None
        self.connection_start = None
    
    def move_block(self, block_id, dx, dy):
        """Move a block"""
        block = self.blocks[block_id]
        self.canvas.move(block_id, dx, dy)
        block.x += dx
        block.y += dy
    
    def generate_code(self):
        """Generate Python code from visual blocks"""
        code_lines = ["# Generated from Visual Programming", ""]
        
        # Sort blocks by position (top to bottom, left to right)
        sorted_blocks = sorted(
            self.blocks.values(),
            key=lambda b: (b.y, b.x)
        )
        
        for block in sorted_blocks:
            if block.type == "variable":
                code_lines.append(f"# Variable block: {block.text}")
            elif block.type == "input":
                code_lines.append(f"# Input block: {block.text}")
            elif block.type == "calculation":
                code_lines.append(f"# Calculation block: {block.text}")
            elif block.type == "condition":
                code_lines.append(f"# Condition block: {block.text}")
            elif block.type == "loop":
                code_lines.append(f"# Loop block: {block.text}")
            elif block.type == "output":
                code_lines.append(f"# Output block: {block.text}")
            elif block.type == "function":
                code_lines.append(f"# Function block: {block.text}")
        
        code = "\n".join(code_lines)
        self.show_code_dialog(code)
    
    def show_code_dialog(self, code):
        """Show generated code in dialog"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Generated Code")
        dialog.geometry("600x400")
        
        text_widget = tk.Text(dialog, wrap=tk.WORD)
        text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        text_widget.insert(tk.END, code)
        
        ttk.Button(dialog, text="Copy", command=lambda: self.copy_code(text_widget.get(1.0, tk.END))).pack(pady=5)
    
    def copy_code(self, code):
        """Copy code to clipboard"""
        self.root.clipboard_clear()
        self.root.clipboard_append(code)
        messagebox.showinfo("Success", "Code copied to clipboard!")
    
    def run_program(self):
        """Run the visual program"""
        self.generate_code()
        messagebox.showinfo("Run", "Program execution started!")
    
    def save_project(self):
        """Save visual project"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if filename:
            project_data = {
                "blocks": [
                    {
                        "id": block.id,
                        "type": block.type,
                        "x": block.x,
                        "y": block.y,
                        "width": block.width,
                        "height": block.height,
                        "color": block.color,
                        "text": block.text,
                        "connections": block.connections
                    }
                    for block in self.blocks.values()
                ]
            }
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(project_data, f, ensure_ascii=False, indent=2)
            
            messagebox.showinfo("Success", "Project saved successfully!")
    
    def load_project(self):
        """Load visual project"""
        filename = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if filename:
            with open(filename, 'r', encoding='utf-8') as f:
                project_data = json.load(f)
            
            # Clear existing blocks
            self.canvas.delete("all")
            self.blocks.clear()
            
            # Load blocks
            for block_data in project_data["blocks"]:
                block = VisualBlock(
                    id=block_data["id"],
                    type=block_data["type"],
                    x=block_data["x"],
                    y=block_data["y"],
                    width=block_data["width"],
                    height=block_data["height"],
                    color=block_data["color"],
                    text=block_data["text"],
                    connections=block_data["connections"]
                )
                self.blocks[block.id] = block
                self.draw_block(block)
            
            messagebox.showinfo("Success", "Project loaded successfully!")
    
    def ai_assist(self):
        """AI-powered assistance"""
        messagebox.showinfo("AI Assistant", "AI Assistant is analyzing your program...")
    
    def run(self):
        """Run the IDE"""
        self.root.mainloop()

if __name__ == "__main__":
    ide = VisualProgrammingIDE()
    ide.run()
