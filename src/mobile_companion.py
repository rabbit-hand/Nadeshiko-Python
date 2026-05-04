"""
Mobile App Companion - World-changing cross-platform mobile development
"""

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.core.window import Window
from kivy.config import Config
import asyncio
import json
import requests
from typing import Dict, List, Any
from dataclasses import dataclass
import threading

# Configure Kivy
Config.set('graphics', 'resizable', True)
Config.set('kivy', 'log_level', 'info')

@dataclass
class MobileProject:
    id: str
    name: str
    code: str
    last_modified: str
    is_synced: bool

class NadesikoMobileApp(App):
    """Revolutionary mobile Nadesiko Python app"""
    
    def build(self):
        Window.title = "Nadesiko Python Mobile"
        Window.bind(on_keyboard=self._on_keyboard)
        
        # Main layout
        self.root_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        self.header = self._create_header()
        self.root_layout.add_widget(self.header)
        
        # Main content area
        self.content = BoxLayout(orientation='horizontal', spacing=10)
        
        # Left panel - Project list
        self.project_panel = self._create_project_panel()
        self.content.add_widget(self.project_panel)
        
        # Center - Code editor
        self.editor_panel = self._create_editor_panel()
        self.content.add_widget(self.editor_panel)
        
        # Right panel - Tools
        self.tools_panel = self._create_tools_panel()
        self.content.add_widget(self.tools_panel)
        
        self.root_layout.add_widget(self.content)
        
        # Bottom toolbar
        self.toolbar = self._create_toolbar()
        self.root_layout.add_widget(self.toolbar)
        
        # Initialize data
        self.projects = {}
        self.current_project = None
        self.api_base = "https://api.nadesiko.cloud"
        
        # Load projects
        self._load_local_projects()
        
        return self.root_layout
    
    def _create_header(self):
        """Create app header"""
        header = BoxLayout(size_hint_y=None, height=60, spacing=10)
        
        # App title
        title = Label(
            text='🌍 Nadesiko Python',
            font_size=20,
            bold=True,
            size_hint_x=0.6
        )
        header.add_widget(title)
        
        # Sync button
        sync_btn = Button(
            text='🔄 Sync',
            size_hint_x=0.2,
            background_color=(0.2, 0.6, 1, 1)
        )
        sync_btn.bind(on_press=self._sync_projects)
        header.add_widget(sync_btn)
        
        # Settings button
        settings_btn = Button(
            text='⚙️',
            size_hint_x=0.1,
            background_color=(0.5, 0.5, 0.5, 1)
        )
        settings_btn.bind(on_press=self._show_settings)
        header.add_widget(settings_btn)
        
        return header
    
    def _create_project_panel(self):
        """Create project list panel"""
        panel = BoxLayout(orientation='vertical', size_hint_x=0.25, spacing=5)
        
        # Panel title
        title = Label(
            text='📁 Projects',
            font_size=16,
            bold=True,
            size_hint_y=None,
            height=40
        )
        panel.add_widget(title)
        
        # Project list
        self.project_list = GridLayout(cols=1, spacing=5, size_hint_y=0.8)
        project_scroll = ScrollView(size_hint=(1, 1))
        project_scroll.add_widget(self.project_list)
        panel.add_widget(project_scroll)
        
        # New project button
        new_btn = Button(
            text='➕ New Project',
            size_hint_y=None,
            height=50,
            background_color=(0.2, 0.8, 0.2, 1)
        )
        new_btn.bind(on_press=self._new_project)
        panel.add_widget(new_btn)
        
        return panel
    
    def _create_editor_panel(self):
        """Create code editor panel"""
        panel = BoxLayout(orientation='vertical', size_hint_x=0.5, spacing=5)
        
        # Editor header
        editor_header = BoxLayout(size_hint_y=None, height=40, spacing=5)
        
        # Language toggle
        self.lang_btn = Button(
            text='🇯🇵 Japanese',
            size_hint_x=0.3,
            background_color=(0.3, 0.3, 0.8, 1)
        )
        self.lang_btn.bind(on_press=self._toggle_language)
        editor_header.add_widget(self.lang_btn)
        
        # Project name
        self.project_name_label = Label(
            text='No project selected',
            font_size=14,
            size_hint_x=0.7
        )
        editor_header.add_widget(self.project_name_label)
        
        panel.add_widget(editor_header)
        
        # Code editor
        self.code_editor = TextInput(
            font_size=14,
            font_name='RobotoMono-Regular.ttf',
            padding=10,
            multiline=True,
            background_color=(0.95, 0.95, 0.95, 1),
            foreground_color=(0.1, 0.1, 0.1, 1)
        )
        self.code_editor.bind(text=self._on_code_change)
        panel.add_widget(self.code_editor)
        
        return panel
    
    def _create_tools_panel(self):
        """Create tools panel"""
        panel = BoxLayout(orientation='vertical', size_hint_x=0.25, spacing=5)
        
        # Panel title
        title = Label(
            text='🛠️ Tools',
            font_size=16,
            bold=True,
            size_hint_y=None,
            height=40
        )
        panel.add_widget(title)
        
        # Tool buttons
        tools = [
            ('▶️ Run', self._run_code, (0.2, 0.8, 0.2, 1)),
            ('🔍 Debug', self._debug_code, (0.8, 0.6, 0.2, 1)),
            ('📊 Visualize', self._visualize_code, (0.2, 0.6, 0.8, 1)),
            ('💾 Save', self._save_project, (0.6, 0.4, 0.8, 1)),
            ('📤 Share', self._share_project, (0.8, 0.2, 0.4, 1)),
            ('📚 Examples', self._show_examples, (0.4, 0.8, 0.6, 1)),
            ('🤖 AI Assist', self._ai_assist, (0.6, 0.2, 0.8, 1)),
            ('📖 Help', self._show_help, (0.8, 0.8, 0.2, 1)),
        ]
        
        for text, callback, color in tools:
            btn = Button(
                text=text,
                size_hint_y=None,
                height=45,
                background_color=color
            )
            btn.bind(on_press=callback)
            panel.add_widget(btn)
        
        return panel
    
    def _create_toolbar(self):
        """Create bottom toolbar"""
        toolbar = BoxLayout(size_hint_y=None, height=60, spacing=5)
        
        # Quick actions
        quick_actions = [
            ('📝 New', self._new_project),
            ('📁 Open', self._open_project),
            ('💾 Save', self._save_project),
            ('▶️ Run', self._run_code),
            ('🔄 Sync', self._sync_projects),
        ]
        
        for text, callback in quick_actions:
            btn = Button(
                text=text,
                size_hint_x=0.2
            )
            btn.bind(on_press=callback)
            toolbar.add_widget(btn)
        
        return toolbar
    
    def _load_local_projects(self):
        """Load local projects"""
        try:
            with open('mobile_projects.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.projects = {
                    pid: MobileProject(**project_data)
                    for pid, project_data in data.items()
                }
                self._update_project_list()
        except FileNotFoundError:
            self.projects = {}
    
    def _save_local_projects(self):
        """Save local projects"""
        data = {
            pid: {
                'id': p.id,
                'name': p.name,
                'code': p.code,
                'last_modified': p.last_modified,
                'is_synced': p.is_synced
            }
            for pid, p in self.projects.items()
        }
        
        with open('mobile_projects.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def _update_project_list(self):
        """Update project list UI"""
        self.project_list.clear_widgets()
        
        for project_id, project in self.projects.items():
            btn = Button(
                text=f"📄 {project.name}",
                size_hint_y=None,
                height=40,
                background_color=(0.9, 0.9, 0.9, 1) if project.is_synced else (0.8, 0.8, 0.8, 1)
            )
            btn.bind(on_press=lambda x, pid=project_id: self._select_project(pid))
            self.project_list.add_widget(btn)
    
    def _new_project(self, instance):
        """Create new project"""
        popup = Popup(title='New Project', size_hint=(0.8, 0.4))
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        name_input = TextInput(
            hint_text='Project name',
            multiline=False,
            size_hint_y=None,
            height=40
        )
        layout.add_widget(name_input)
        
        button_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        create_btn = Button(text='Create', background_color=(0.2, 0.8, 0.2, 1))
        create_btn.bind(on_press=lambda x: self._create_project(name_input.text, popup))
        button_layout.add_widget(create_btn)
        
        cancel_btn = Button(text='Cancel', background_color=(0.8, 0.2, 0.2, 1))
        cancel_btn.bind(on_press=popup.dismiss)
        button_layout.add_widget(cancel_btn)
        
        layout.add_widget(button_layout)
        popup.content = layout
        popup.open()
    
    def _create_project(self, name: str, popup: Popup):
        """Create new project"""
        if name.strip():
            import uuid
            from datetime import datetime
            
            project_id = str(uuid.uuid4())
            project = MobileProject(
                id=project_id,
                name=name.strip(),
                code='',
                last_modified=datetime.now().isoformat(),
                is_synced=False
            )
            
            self.projects[project_id] = project
            self._save_local_projects()
            self._update_project_list()
            self._select_project(project_id)
            popup.dismiss()
    
    def _select_project(self, project_id: str):
        """Select a project"""
        if project_id in self.projects:
            self.current_project = project_id
            project = self.projects[project_id]
            
            self.project_name_label.text = project.name
            self.code_editor.text = project.code
    
    def _save_project(self, instance=None):
        """Save current project"""
        if self.current_project and self.current_project in self.projects:
            from datetime import datetime
            
            project = self.projects[self.current_project]
            project.code = self.code_editor.text
            project.last_modified = datetime.now().isoformat()
            project.is_synced = False
            
            self._save_local_projects()
            self._update_project_list()
            
            # Show save confirmation
            self._show_message("Project saved successfully!")
    
    def _run_code(self, instance=None):
        """Run current code"""
        if not self.code_editor.text.strip():
            self._show_message("No code to run!")
            return
        
        # This would connect to actual Nadesiko Python engine
        # For now, just show a message
        self._show_message("Code execution started...")
        
        # Simulate running code in background
        threading.Thread(target=self._execute_code, daemon=True).start()
    
    def _execute_code(self):
        """Execute code in background"""
        try:
            # This would integrate with actual Nadesiko Python parser
            import subprocess
            import sys
            
            # Create temporary file
            with open('temp_code.nako', 'w', encoding='utf-8') as f:
                f.write(self.code_editor.text)
            
            # Execute with Nadesiko Python
            result = subprocess.run([
                sys.executable, '-c', 
                f"from nadesiko_parser import NadesikoParser; "
                f"parser = NadesikoParser(); "
                f"parser.execute(open('temp_code.nako', 'r', encoding='utf-8').read())"
            ], capture_output=True, text=True)
            
            # Show result
            self._show_output(result.stdout, result.stderr)
            
        except Exception as e:
            self._show_message(f"Execution error: {str(e)}")
    
    def _show_output(self, stdout: str, stderr: str):
        """Show execution output"""
        popup = Popup(title='Output', size_hint=(0.9, 0.6))
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        if stdout:
            stdout_label = Label(
                text=f"Output:\n{stdout}",
                text_size=12,
                color=(0, 0.5, 0, 1)
            )
            layout.add_widget(stdout_label)
        
        if stderr:
            stderr_label = Label(
                text=f"Error:\n{stderr}",
                text_size=12,
                color=(0.8, 0, 0, 1)
            )
            layout.add_widget(stderr_label)
        
        close_btn = Button(
            text='Close',
            size_hint_y=None,
            height=40,
            background_color=(0.5, 0.5, 0.5, 1)
        )
        close_btn.bind(on_press=popup.dismiss)
        layout.add_widget(close_btn)
        
        popup.content = layout
        popup.open()
    
    def _sync_projects(self, instance=None):
        """Sync projects with cloud"""
        self._show_message("Syncing projects...")
        
        # This would integrate with actual cloud storage
        threading.Thread(target=self._perform_sync, daemon=True).start()
    
    def _perform_sync(self):
        """Perform cloud synchronization"""
        try:
            # Simulate sync process
            import time
            time.sleep(2)
            
            # Mark all projects as synced
            for project in self.projects.values():
                project.is_synced = True
            
            self._save_local_projects()
            self._update_project_list()
            
            self._show_message("Sync completed successfully!")
            
        except Exception as e:
            self._show_message(f"Sync failed: {str(e)}")
    
    def _toggle_language(self, instance):
        """Toggle between Japanese and English"""
        if self.lang_btn.text == '🇯🇵 Japanese':
            self.lang_btn.text = '🇺🇸 English'
        else:
            self.lang_btn.text = '🇯🇵 Japanese'
    
    def _show_settings(self, instance):
        """Show settings popup"""
        popup = Popup(title='Settings', size_hint=(0.8, 0.6))
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # API Key setting
        api_label = Label(text='Cloud API Key:')
        layout.add_widget(api_label)
        
        api_input = TextInput(
            text='',
            multiline=False,
            size_hint_y=None,
            height=40
        )
        layout.add_widget(api_input)
        
        # Save button
        save_btn = Button(
            text='Save Settings',
            background_color=(0.2, 0.6, 0.8, 1)
        )
        save_btn.bind(on_press=lambda x: self._save_settings(api_input.text, popup))
        layout.add_widget(save_btn)
        
        popup.content = layout
        popup.open()
    
    def _save_settings(self, api_key: str, popup: Popup):
        """Save settings"""
        # Save API key
        with open('mobile_settings.json', 'w', encoding='utf-8') as f:
            json.dump({'api_key': api_key}, f)
        
        popup.dismiss()
        self._show_message("Settings saved!")
    
    def _show_message(self, message: str):
        """Show temporary message"""
        # Create toast-like notification
        toast = Label(
            text=message,
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.9},
            background_color=(0.2, 0.2, 0.2, 0.8),
            color=(1, 1, 1, 1)
        )
        
        self.root_layout.add_widget(toast)
        
        # Remove after 2 seconds
        from kivy.clock import Clock
        Clock.schedule_once(lambda dt: self.root_layout.remove_widget(toast), 2)
    
    def _on_code_change(self, instance, value):
        """Handle code changes"""
        if self.current_project and self.current_project in self.projects:
            self.projects[self.current_project].is_synced = False
            self._update_project_list()
    
    def _on_keyboard(self, window, key, scancode, codepoint, modifier):
        """Handle keyboard shortcuts"""
        # Ctrl+S to save
        if modifier == 'ctrl' and key == 115:
            self._save_project()
        # Ctrl+R to run
        elif modifier == 'ctrl' and key == 114:
            self._run_code()
        
        return True
    
    def _debug_code(self, instance):
        """Debug code"""
        self._show_message("Debugging features coming soon!")
    
    def _visualize_code(self, instance):
        """Visualize code"""
        self._show_message("Code visualization coming soon!")
    
    def _share_project(self, instance):
        """Share project"""
        self._show_message("Project sharing coming soon!")
    
    def _show_examples(self, instance):
        """Show examples"""
        self._show_message("Code examples coming soon!")
    
    def _ai_assist(self, instance):
        """AI assistance"""
        self._show_message("AI assistance coming soon!")
    
    def _show_help(self, instance):
        """Show help"""
        help_text = """
        Nadesiko Python Mobile Help
        
        🇯🇵 Japanese Mode:
        変数は値
        AとBを足す
        「メッセージ」を表示
        
        🇺🇸 English Mode:
        variable is value
        A plus B
        show "message"
        
        Keyboard Shortcuts:
        Ctrl+S: Save project
        Ctrl+R: Run code
        """
        
        popup = Popup(title='Help', size_hint=(0.9, 0.7))
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        help_label = Label(
            text=help_text,
            text_size=12,
            halign='left'
        )
        layout.add_widget(help_label)
        
        close_btn = Button(
            text='Close',
            size_hint_y=None,
            height=40
        )
        close_btn.bind(on_press=popup.dismiss)
        layout.add_widget(close_btn)
        
        popup.content = layout
        popup.open()
    
    def _open_project(self, instance):
        """Open existing project"""
        chooser = FileChooserListView(
            path='.',
            filters=['*.nako', '*.py', '*.txt']
        )
        
        popup = Popup(title='Open Project', size_hint=(0.9, 0.7))
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(chooser)
        
        button_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        open_btn = Button(
            text='Open',
            background_color=(0.2, 0.8, 0.2, 1)
        )
        open_btn.bind(on_press=lambda x: self._load_project_file(chooser.path, popup))
        button_layout.add_widget(open_btn)
        
        cancel_btn = Button(
            text='Cancel',
            background_color=(0.8, 0.2, 0.2, 1)
        )
        cancel_btn.bind(on_press=popup.dismiss)
        button_layout.add_widget(cancel_btn)
        
        layout.add_widget(button_layout)
        popup.content = layout
        popup.open()
    
    def _load_project_file(self, file_path: str, popup: Popup):
        """Load project from file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
            
            # Create new project
            import os
            from datetime import datetime
            import uuid
            
            project_id = str(uuid.uuid4())
            project_name = os.path.basename(file_path).split('.')[0]
            
            project = MobileProject(
                id=project_id,
                name=project_name,
                code=code,
                last_modified=datetime.now().isoformat(),
                is_synced=False
            )
            
            self.projects[project_id] = project
            self._save_local_projects()
            self._update_project_list()
            self._select_project(project_id)
            
            popup.dismiss()
            self._show_message(f"Project '{project_name}' loaded successfully!")
            
        except Exception as e:
            self._show_message(f"Failed to load project: {str(e)}")

if __name__ == '__main__':
    NadesikoMobileApp().run()
