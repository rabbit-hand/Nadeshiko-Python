"""
Advanced Debugging and Visualization Tools - World-changing development experience
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import threading
import time
import json
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass
from collections import defaultdict
import networkx as nx
from matplotlib.patches import Rectangle, FancyBboxPatch
import matplotlib.patches as mpatches

@dataclass
class ExecutionStep:
    line_number: int
    code: str
    variables: Dict[str, Any]
    output: str
    timestamp: float
    type: str  # 'assignment', 'calculation', 'condition', 'loop', 'function'

@dataclass
class DebugEvent:
    type: str  # 'breakpoint', 'variable_change', 'error', 'warning'
    line_number: int
    message: str
    data: Any
    timestamp: float

class ExecutionVisualizer:
    """Advanced execution visualization"""
    
    def __init__(self):
        self.execution_steps = []
        self.debug_events = []
        self.current_step = 0
        self.animation_speed = 1.0
        self.breakpoints = set()
        
    def add_execution_step(self, step: ExecutionStep):
        """Add execution step"""
        self.execution_steps.append(step)
    
    def add_debug_event(self, event: DebugEvent):
        """Add debug event"""
        self.debug_events.append(event)
    
    def set_breakpoint(self, line_number: int):
        """Set breakpoint"""
        self.breakpoints.add(line_number)
    
    def remove_breakpoint(self, line_number: int):
        """Remove breakpoint"""
        self.breakpoints.discard(line_number)
    
    def visualize_execution(self, code_lines: List[str]) -> 'Figure':
        """Create execution visualization"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Nadesiko Python Execution Visualization', fontsize=16, fontweight='bold')
        
        # Code execution flow
        self._plot_execution_flow(axes[0, 0], code_lines)
        
        # Variable timeline
        self._plot_variable_timeline(axes[0, 1])
        
        # Memory usage
        self._plot_memory_usage(axes[1, 0])
        
        # Execution speed
        self._plot_execution_speed(axes[1, 1])
        
        plt.tight_layout()
        return fig
    
    def _plot_execution_flow(self, ax, code_lines: List[str]):
        """Plot code execution flow"""
        ax.set_title('Code Execution Flow', fontweight='bold')
        ax.set_xlabel('Time')
        ax.set_ylabel('Line Number')
        
        if not self.execution_steps:
            ax.text(0.5, 0.5, 'No execution data', 
                    transform=ax.transAxes, ha='center', va='center')
            return
        
        # Create execution flow
        x_positions = []
        y_positions = []
        colors = []
        
        for i, step in enumerate(self.execution_steps):
            x_positions.append(step.timestamp)
            y_positions.append(step.line_number)
            
            # Color by step type
            color_map = {
                'assignment': 'blue',
                'calculation': 'green',
                'condition': 'orange',
                'loop': 'red',
                'function': 'purple'
            }
            colors.append(color_map.get(step.type, 'gray'))
        
        # Plot execution path
        ax.plot(x_positions, y_positions, 'o-', linewidth=2, markersize=6)
        
        # Add color legend
        for step_type, color in color_map.items():
            ax.scatter([], [], c=color, label=step_type, s=100)
        
        ax.legend(loc='upper right')
        ax.grid(True, alpha=0.3)
        
        # Mark breakpoints
        for bp_line in self.breakpoints:
            ax.axhline(y=bp_line, color='red', linestyle='--', alpha=0.5)
            ax.text(0.02, bp_line, 'BREAKPOINT', 
                    transform=ax.get_yaxis_transform(),
                    fontsize=8, color='red', va='bottom')
    
    def _plot_variable_timeline(self, ax):
        """Plot variable changes over time"""
        ax.set_title('Variable Timeline', fontweight='bold')
        ax.set_xlabel('Time')
        ax.set_ylabel('Variable Value')
        
        if not self.execution_steps:
            ax.text(0.5, 0.5, 'No variable data', 
                    transform=ax.transAxes, ha='center', va='center')
            return
        
        # Track variable changes
        variable_history = defaultdict(list)
        time_history = defaultdict(list)
        
        for step in self.execution_steps:
            for var_name, var_value in step.variables.items():
                variable_history[var_name].append(var_value)
                time_history[var_name].append(step.timestamp)
        
        # Plot each variable
        colors = plt.cm.tab10(np.linspace(0, 1, len(variable_history)))
        
        for i, (var_name, values) in enumerate(variable_history.items()):
            if var_name in time_history:
                ax.plot(time_history[var_name], values, 
                        'o-', label=var_name, color=colors[i], linewidth=2)
        
        ax.legend(loc='best')
        ax.grid(True, alpha=0.3)
    
    def _plot_memory_usage(self, ax):
        """Plot memory usage"""
        ax.set_title('Memory Usage', fontweight='bold')
        ax.set_xlabel('Time')
        ax.set_ylabel('Memory (MB)')
        
        # Simulate memory usage based on variable count
        memory_usage = []
        timestamps = []
        
        for step in self.execution_steps:
            memory_usage.append(len(step.variables) * 0.1)  # Simulated memory
            timestamps.append(step.timestamp)
        
        if memory_usage:
            ax.fill_between(timestamps, 0, memory_usage, alpha=0.3, color='blue')
            ax.plot(timestamps, memory_usage, 'b-', linewidth=2)
        
        ax.grid(True, alpha=0.3)
    
    def _plot_execution_speed(self, ax):
        """Plot execution speed"""
        ax.set_title('Execution Speed', fontweight='bold')
        ax.set_xlabel('Step Number')
        ax.set_ylabel('Time per Step (ms)')
        
        if len(self.execution_steps) < 2:
            ax.text(0.5, 0.5, 'Insufficient data', 
                    transform=ax.transAxes, ha='center', va='center')
            return
        
        # Calculate execution speed
        step_times = []
        for i in range(1, len(self.execution_steps)):
            time_diff = (self.execution_steps[i].timestamp - 
                        self.execution_steps[i-1].timestamp) * 1000
            step_times.append(time_diff)
        
        step_numbers = range(1, len(step_times) + 1)
        
        ax.bar(step_numbers, step_times, alpha=0.7, color='green')
        ax.axhline(y=np.mean(step_times), color='red', 
                   linestyle='--', label=f'Average: {np.mean(step_times):.2f}ms')
        
        ax.legend()
        ax.grid(True, alpha=0.3)

class DebugVisualizerGUI:
    """GUI for debugging and visualization"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Nadesiko Python - Advanced Debug Visualizer")
        self.root.geometry("1400x900")
        
        self.visualizer = ExecutionVisualizer()
        self.current_code = []
        self.animation_running = False
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the GUI"""
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left panel - Code and controls
        left_panel = ttk.Frame(main_frame, width=400)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 5))
        
        # Code editor
        self.setup_code_editor(left_panel)
        
        # Debug controls
        self.setup_debug_controls(left_panel)
        
        # Right panel - Visualization
        right_panel = ttk.Frame(main_frame)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.setup_visualization_panel(right_panel)
        
    def setup_code_editor(self, parent):
        """Setup code editor with line numbers"""
        editor_frame = ttk.LabelFrame(parent, text="Code Editor")
        editor_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Create text widget with line numbers
        text_frame = ttk.Frame(editor_frame)
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        # Line numbers
        self.line_numbers = tk.Text(text_frame, width=4, padx=3, takefocus=0,
                                   borderwidth=0, state='disabled', wrap='none')
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)
        
        # Code text
        self.code_text = tk.Text(text_frame, wrap='none', undo=True,
                               font=('Consolas', 11))
        self.code_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(text_frame, orient='vertical', command=self.on_textscroll)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.code_text.config(yscrollcommand=scrollbar.set)
        self.line_numbers.config(yscrollcommand=scrollbar.set)
        
        # Bind events
        self.code_text.bind('<KeyRelease>', self.on_key_release)
        self.code_text.bind('<Button-1>', self.on_click)
        self.code_text.bind('<Configure>', self.on_configure)
        
        # Add sample code
        sample_code = """Aは10
Bは20
CはAとBを足す
「結果: {C}」を表示

もしCが30以上ならば
    「大きい値です」を表示
そうでなければ
    「小さい値です」を表示

5回繰り返す
    「カウント: {回数}」を表示
    回数は回数と1を足す"""
        
        self.code_text.insert('1.0', sample_code)
        self.update_line_numbers()
        
    def setup_debug_controls(self, parent):
        """Setup debug control panel"""
        control_frame = ttk.LabelFrame(parent, text="Debug Controls")
        control_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Execution controls
        exec_frame = ttk.Frame(control_frame)
        exec_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(exec_frame, text="▶️ Run", 
                  command=self.run_code).pack(side=tk.LEFT, padx=2)
        ttk.Button(exec_frame, text="⏸️ Pause", 
                  command=self.pause_animation).pack(side=tk.LEFT, padx=2)
        ttk.Button(exec_frame, text="⏹️ Stop", 
                  command=self.stop_animation).pack(side=tk.LEFT, padx=2)
        ttk.Button(exec_frame, text="🔄 Reset", 
                  command=self.reset_visualization).pack(side=tk.LEFT, padx=2)
        
        # Breakpoint controls
        bp_frame = ttk.Frame(control_frame)
        bp_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(bp_frame, text="Breakpoints:").pack(side=tk.LEFT)
        self.bp_label = ttk.Label(bp_frame, text="None set")
        self.bp_label.pack(side=tk.LEFT, padx=10)
        
        ttk.Button(bp_frame, text="📍 Toggle BP", 
                  command=self.toggle_breakpoint).pack(side=tk.RIGHT)
        
        # Speed control
        speed_frame = ttk.Frame(control_frame)
        speed_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(speed_frame, text="Animation Speed:").pack(side=tk.LEFT)
        self.speed_var = tk.DoubleVar(value=1.0)
        speed_scale = ttk.Scale(speed_frame, from_=0.1, to=5.0, 
                               variable=self.speed_var, orient='horizontal')
        speed_scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)
        
        # Debug options
        options_frame = ttk.Frame(control_frame)
        options_frame.pack(fill=tk.X, pady=5)
        
        self.show_variables = tk.BooleanVar(value=True)
        self.show_memory = tk.BooleanVar(value=True)
        self.show_flow = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(options_frame, text="Show Variables", 
                     variable=self.show_variables).pack(anchor='w')
        ttk.Checkbutton(options_frame, text="Show Memory", 
                     variable=self.show_memory).pack(anchor='w')
        ttk.Checkbutton(options_frame, text="Show Flow", 
                     variable=self.show_flow).pack(anchor='w')
        
    def setup_visualization_panel(self, parent):
        """Setup visualization panel"""
        viz_frame = ttk.LabelFrame(parent, text="Execution Visualization")
        viz_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create matplotlib figure
        self.fig, self.axes = plt.subplots(2, 2, figsize=(12, 8))
        self.fig.suptitle('Nadesiko Python Execution Visualization', 
                          fontsize=14, fontweight='bold')
        
        # Embed in tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, viz_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Navigation toolbar
        toolbar_frame = ttk.Frame(viz_frame)
        toolbar_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Button(toolbar_frame, text="⬅️ Previous", 
                  command=self.previous_step).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar_frame, text="⬇️ Next", 
                  command=self.next_step).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar_frame, text="🎬 Play", 
                  command=self.play_animation).pack(side=tk.LEFT, padx=2)
        
        # Step counter
        self.step_label = ttk.Label(toolbar_frame, text="Step: 0/0")
        self.step_label.pack(side=tk.RIGHT, padx=10)
        
    def update_line_numbers(self):
        """Update line numbers"""
        self.line_numbers.config(state='normal')
        self.line_numbers.delete('1.0', 'end')
        
        # Get line count
        line_count = int(self.code_text.index('end-1c').split('.')[0])
        
        # Generate line numbers
        line_numbers_text = '\n'.join(str(i) for i in range(1, line_count + 1))
        self.line_numbers.insert('1.0', line_numbers_text)
        self.line_numbers.config(state='disabled')
        
    def on_textscroll(self, *args):
        """Handle text scrolling"""
        self.line_numbers.yview_moveto(args[0])
        self.code_text.yview_moveto(args[0])
        
    def on_key_release(self, event):
        """Handle key release events"""
        self.update_line_numbers()
        
        # Toggle breakpoint with F9
        if event.keysym == 'F9':
            self.toggle_breakpoint()
        
    def on_click(self, event):
        """Handle mouse click"""
        # Update line highlight
        line_number = int(self.code_text.index(f"@{event.x},{event.y}").split('.')[0])
        self.highlight_line(line_number)
        
    def on_configure(self, event):
        """Handle configure event"""
        self.update_line_numbers()
        
    def highlight_line(self, line_number):
        """Highlight a specific line"""
        # Remove previous highlights
        self.code_text.tag_remove('current_line', '1.0', 'end')
        
        # Add new highlight
        start_idx = f"{line_number}.0"
        end_idx = f"{line_number}.end"
        self.code_text.tag_add('current_line', start_idx, end_idx)
        self.code_text.tag_config('current_line', background='yellow')
        
    def toggle_breakpoint(self):
        """Toggle breakpoint at current line"""
        # Get current line
        cursor_pos = self.code_text.index('insert')
        line_number = int(cursor_pos.split('.')[0])
        
        # Toggle breakpoint
        if line_number in self.visualizer.breakpoints:
            self.visualizer.remove_breakpoint(line_number)
        else:
            self.visualizer.set_breakpoint(line_number)
        
        self.update_breakpoint_display()
        self.highlight_line(line_number)
        
    def update_breakpoint_display(self):
        """Update breakpoint display"""
        if self.visualizer.breakpoints:
            bp_text = f"Lines: {', '.join(map(str, sorted(self.visualizer.breakpoints)))}"
        else:
            bp_text = "None set"
        
        self.bp_label.config(text=bp_text)
        
    def run_code(self):
        """Run code and generate visualization"""
        # Get code
        code = self.code_text.get('1.0', 'end-1c')
        self.current_code = code.split('\n')
        
        # Simulate execution
        self.simulate_execution()
        
        # Update visualization
        self.update_visualization()
        
    def simulate_execution(self):
        """Simulate code execution"""
        self.visualizer.execution_steps.clear()
        self.visualizer.debug_events.clear()
        
        variables = {}
        current_time = 0
        
        for i, line in enumerate(self.current_code):
            if not line.strip() or line.strip().startswith('#'):
                continue
                
            # Parse and execute line
            step_type, new_vars, output = self.parse_line(line, variables)
            
            if new_vars:
                variables.update(new_vars)
            
            # Create execution step
            step = ExecutionStep(
                line_number=i + 1,
                code=line.strip(),
                variables=variables.copy(),
                output=output,
                timestamp=current_time,
                type=step_type
            )
            
            self.visualizer.add_execution_step(step)
            
            # Check for breakpoints
            if (i + 1) in self.visualizer.breakpoints:
                debug_event = DebugEvent(
                    type='breakpoint',
                    line_number=i + 1,
                    message='Breakpoint hit',
                    data=variables.copy(),
                    timestamp=current_time
                )
                self.visualizer.add_debug_event(debug_event)
            
            current_time += 0.1  # Simulate execution time
    
    def parse_line(self, line: str, variables: Dict[str, Any]) -> Tuple[str, Dict[str, Any], str]:
        """Parse a line of Nadesiko code"""
        line = line.strip()
        
        # Variable assignment
        if 'は' in line:
            parts = line.split('は', 1)
            if len(parts) == 2:
                var_name = parts[0].strip()
                try:
                    value = eval(parts[1].strip())
                    return 'assignment', {var_name: value}, f"Assigned {var_name} = {value}"
                except:
                    value = parts[1].strip()
                    return 'assignment', {var_name: value}, f"Assigned {var_name} = {value}"
        
        # Calculation
        elif 'と' in line and ('足す' in line or '掛ける' in line):
            if '足す' in line:
                parts = line.split('と', 1)
                if len(parts) == 2:
                    var1 = parts[0].strip()
                    rest = parts[1]
                    if 'を足す' in rest:
                        var2 = rest.split('を足す')[0].strip()
                        if var1 in variables and var2 in variables:
                            result = variables[var1] + variables[var2]
                            return 'calculation', {'result': result}, f"Calculated {var1} + {var2} = {result}"
        
        # Display
        elif 'を表示' in line or '表示する' in line:
            return 'output', {}, "Output displayed"
        
        # Condition
        elif 'もし' in line:
            return 'condition', {}, "Conditional check"
        
        # Loop
        elif '繰り返す' in line:
            return 'loop', {}, "Loop iteration"
        
        return 'unknown', {}, "Unknown operation"
    
    def update_visualization(self):
        """Update the visualization"""
        # Clear previous plots
        for ax in self.axes.flat:
            ax.clear()
        
        # Create new visualization
        self.visualizer.visualize_execution(self.current_code)
        
        # Update canvas
        self.canvas.draw()
        
        # Update step counter
        total_steps = len(self.visualizer.execution_steps)
        self.step_label.config(text=f"Step: {self.visualizer.current_step}/{total_steps}")
        
    def play_animation(self):
        """Play execution animation"""
        if not self.animation_running:
            self.animation_running = True
            self.visualizer.current_step = 0
            self.animate_execution()
        
    def animate_execution(self):
        """Animate execution step by step"""
        if not self.animation_running or self.visualizer.current_step >= len(self.visualizer.execution_steps):
            self.animation_running = False
            return
        
        # Update to current step
        self.update_step_display(self.visualizer.current_step)
        self.visualizer.current_step += 1
        
        # Schedule next step
        delay = int(1000 / self.speed_var.get())
        self.root.after(delay, self.animate_execution)
        
    def update_step_display(self, step_index):
        """Update display for specific step"""
        if 0 <= step_index < len(self.visualizer.execution_steps):
            step = self.visualizer.execution_steps[step_index]
            
            # Highlight current line
            self.highlight_line(step.line_number)
            
            # Update variable display (would need to add this UI element)
            print(f"Step {step_index + 1}: {step.code}")
            print(f"Variables: {step.variables}")
            if step.output:
                print(f"Output: {step.output}")
    
    def pause_animation(self):
        """Pause animation"""
        self.animation_running = False
        
    def stop_animation(self):
        """Stop animation"""
        self.animation_running = False
        self.visualizer.current_step = 0
        
    def reset_visualization(self):
        """Reset visualization"""
        self.animation_running = False
        self.visualizer.current_step = 0
        self.visualizer.execution_steps.clear()
        self.visualizer.debug_events.clear()
        self.update_visualization()
        
    def previous_step(self):
        """Go to previous step"""
        if self.visualizer.current_step > 0:
            self.visualizer.current_step -= 1
            self.update_step_display(self.visualizer.current_step)
            
    def next_step(self):
        """Go to next step"""
        if self.visualizer.current_step < len(self.visualizer.execution_steps) - 1:
            self.visualizer.current_step += 1
            self.update_step_display(self.visualizer.current_step)
    
    def run(self):
        """Run the GUI"""
        self.root.mainloop()

if __name__ == "__main__":
    app = DebugVisualizerGUI()
    app.run()
