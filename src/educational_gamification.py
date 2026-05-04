"""
Educational Gamification System - World-changing learning experience
"""

import json
import time
import math
import random
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, messagebox

class AchievementType(Enum):
    CODE_LINES = "code_lines"
    FUNCTIONS = "functions"
    PROJECTS = "projects"
    COLLABORATIONS = "collaborations"
    STREAK_DAYS = "streak_days"
    PERFECT_RUN = "perfect_run"
    DEBUG_MASTER = "debug_master"
    CREATIVE_SOLUTIONS = "creative_solutions"

class DifficultyLevel(Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"

@dataclass
class Achievement:
    id: str
    name: str
    description: str
    type: AchievementType
    difficulty: DifficultyLevel
    points: int
    badge_icon: str
    unlocked: bool = False
    unlocked_at: datetime = None
    progress: float = 0.0
    max_progress: float = 100.0

@dataclass
class UserProfile:
    username: str
    level: int
    experience_points: int
    total_points: int
    streak_days: int
    last_active_date: datetime
    achievements: List[str]
    statistics: Dict[str, Any]
    learning_path: str
    preferred_language: str
    avatar: str = "👤"

@dataclass
class Challenge:
    id: str
    title: str
    description: str
    difficulty: DifficultyLevel
    category: str
    tasks: List[str]
    reward_points: int
    time_limit: int  # minutes
    hints: List[str]

@dataclass
class LearningPath:
    id: str
    name: str
    description: str
    difficulty_progression: List[DifficultyLevel]
    modules: List[str]
    estimated_hours: int
    prerequisites: List[str]

class GamificationEngine:
    """Revolutionary educational gamification system"""
    
    def __init__(self):
        self.user_profile = None
        self.achievements = self._initialize_achievements()
        self.challenges = self._initialize_challenges()
        self.learning_paths = self._initialize_learning_paths()
        self.current_session = {
            'start_time': datetime.now(),
            'code_lines': 0,
            'functions_created': 0,
            'projects_completed': 0,
            'errors_fixed': 0,
            'hints_used': 0
        }
        
    def _initialize_achievements(self) -> Dict[str, Achievement]:
        """Initialize all possible achievements"""
        return {
            # Code-related achievements
            "first_lines": Achievement(
                id="first_lines",
                name="First Steps",
                description="Write your first 10 lines of code",
                type=AchievementType.CODE_LINES,
                difficulty=DifficultyLevel.BEGINNER,
                points=10,
                badge_icon="🌱"
            ),
            "code_warrior": Achievement(
                id="code_warrior",
                name="Code Warrior",
                description="Write 1000 lines of code",
                type=AchievementType.CODE_LINES,
                difficulty=DifficultyLevel.INTERMEDIATE,
                points=100,
                badge_icon="⚔️"
            ),
            "code_master": Achievement(
                id="code_master",
                name="Code Master",
                description="Write 5000 lines of code",
                type=AchievementType.CODE_LINES,
                difficulty=DifficultyLevel.ADVANCED,
                points=500,
                badge_icon="🏆"
            ),
            
            # Function-related achievements
            "first_function": Achievement(
                id="first_function",
                name="Function Creator",
                description="Create your first function",
                type=AchievementType.FUNCTIONS,
                difficulty=DifficultyLevel.BEGINNER,
                points=15,
                badge_icon="🔧"
            ),
            "function_expert": Achievement(
                id="function_expert",
                name="Function Expert",
                description="Create 50 functions",
                type=AchievementType.FUNCTIONS,
                difficulty=DifficultyLevel.INTERMEDIATE,
                points=150,
                badge_icon="⚙️"
            ),
            
            # Project achievements
            "first_project": Achievement(
                id="first_project",
                name="Project Starter",
                description="Complete your first project",
                type=AchievementType.PROJECTS,
                difficulty=DifficultyLevel.BEGINNER,
                points=20,
                badge_icon="📁"
            ),
            "project_builder": Achievement(
                id="project_builder",
                name="Project Builder",
                description="Complete 10 projects",
                type=AchievementType.PROJECTS,
                difficulty=DifficultyLevel.INTERMEDIATE,
                points=200,
                badge_icon="🏗️"
            ),
            
            # Streak achievements
            "week_streak": Achievement(
                id="week_streak",
                name="Week Warrior",
                description="Code for 7 consecutive days",
                type=AchievementType.STREAK_DAYS,
                difficulty=DifficultyLevel.BEGINNER,
                points=50,
                badge_icon="🔥"
            ),
            "month_streak": Achievement(
                id="month_streak",
                name="Month Champion",
                description="Code for 30 consecutive days",
                type=AchievementType.STREAK_DAYS,
                difficulty=DifficultyLevel.ADVANCED,
                points=300,
                badge_icon="💎"
            ),
            
            # Special achievements
            "perfect_run": Achievement(
                id="perfect_run",
                name="Perfect Run",
                description="Execute code without any errors",
                type=AchievementType.PERFECT_RUN,
                difficulty=DifficultyLevel.INTERMEDIATE,
                points=75,
                badge_icon="✨"
            ),
            "debug_master": Achievement(
                id="debug_master",
                name="Debug Master",
                description="Fix 100 bugs using the debugger",
                type=AchievementType.DEBUG_MASTER,
                difficulty=DifficultyLevel.ADVANCED,
                points=250,
                badge_icon="🐛"
            ),
            "creative_coder": Achievement(
                id="creative_coder",
                name="Creative Coder",
                description="Complete 5 creative challenges",
                type=AchievementType.CREATIVE_SOLUTIONS,
                difficulty=DifficultyLevel.INTERMEDIATE,
                points=125,
                badge_icon="🎨"
            ),
        }
    
    def _initialize_challenges(self) -> Dict[str, Challenge]:
        """Initialize programming challenges"""
        return {
            # Beginner challenges
            "hello_world": Challenge(
                id="hello_world",
                title="Hello World Challenge",
                description="Create a program that displays 'Hello World' in 3 different languages",
                difficulty=DifficultyLevel.BEGINNER,
                category="basics",
                tasks=[
                    "Display 'Hello World' in Japanese",
                    "Display 'Hello World' in English",
                    "Display 'Hello World' in one more language of your choice"
                ],
                reward_points=25,
                time_limit=15,
                hints=["Use the '表示' command", "Try 'show' for English"]
            ),
            
            "variable_magic": Challenge(
                id="variable_magic",
                title="Variable Magic",
                description="Create a program that uses variables to perform calculations",
                difficulty=DifficultyLevel.BEGINNER,
                category="variables",
                tasks=[
                    "Create 3 different variables",
                    "Perform addition with variables",
                    "Display the result",
                    "Perform multiplication with variables"
                ],
                reward_points=30,
                time_limit=20,
                hints=["Variables store data", "Use 'は' for assignment"]
            ),
            
            # Intermediate challenges
            "function_factory": Challenge(
                id="function_factory",
                title="Function Factory",
                description="Create 3 useful functions with different purposes",
                difficulty=DifficultyLevel.INTERMEDIATE,
                category="functions",
                tasks=[
                    "Create a calculation function",
                    "Create a string manipulation function",
                    "Create a utility function",
                    "Test all functions with examples"
                ],
                reward_points=75,
                time_limit=45,
                hints=["Functions start with '●'", "Use 'を返す' to return values"]
            ),
            
            "loop_master": Challenge(
                id="loop_master",
                title="Loop Master",
                description="Create programs using different types of loops",
                difficulty=DifficultyLevel.INTERMEDIATE,
                category="control_flow",
                tasks=[
                    "Create a for loop",
                    "Create a while loop",
                    "Create a nested loop",
                    "Use loops to process data"
                ],
                reward_points=80,
                time_limit=40,
                hints=["Use '繰り返す' for loops", "Nesting loops creates powerful patterns"]
            ),
            
            # Advanced challenges
            "data_processor": Challenge(
                id="data_processor",
                title="Data Processor",
                description="Create a program that processes and analyzes data",
                difficulty=DifficultyLevel.ADVANCED,
                category="data",
                tasks=[
                    "Read data from a file",
                    "Process and analyze the data",
                    "Generate meaningful statistics",
                    "Display results in multiple formats"
                ],
                reward_points=150,
                time_limit=90,
                hints=["Use file operations", "Statistical functions can help"]
            ),
            
            "api_integrator": Challenge(
                id="api_integrator",
                title="API Integrator",
                description="Create a program that uses external APIs",
                difficulty=DifficultyLevel.EXPERT,
                category="advanced",
                tasks=[
                    "Connect to a web API",
                    "Process API response",
                    "Handle errors gracefully",
                    "Display results in user-friendly format"
                ],
                reward_points=200,
                time_limit=120,
                hints=["Use HTTP requests", "JSON is common for APIs"]
            ),
        }
    
    def _initialize_learning_paths(self) -> Dict[str, LearningPath]:
        """Initialize structured learning paths"""
        return {
            "beginner_path": LearningPath(
                id="beginner_path",
                name="Programming Fundamentals",
                description="Learn the basics of programming with Nadesiko",
                difficulty_progression=[
                    DifficultyLevel.BEGINNER,
                    DifficultyLevel.BEGINNER,
                    DifficultyLevel.INTERMEDIATE
                ],
                modules=[
                    "variables_and_data",
                    "basic_operations",
                    "input_and_output",
                    "simple_programs"
                ],
                estimated_hours=10,
                prerequisites=[]
            ),
            
            "intermediate_path": LearningPath(
                id="intermediate_path",
                name="Intermediate Programming",
                description="Master control flow and functions",
                difficulty_progression=[
                    DifficultyLevel.INTERMEDIATE,
                    DifficultyLevel.INTERMEDIATE,
                    DifficultyLevel.ADVANCED
                ],
                modules=[
                    "control_structures",
                    "function_development",
                    "error_handling",
                    "file_operations"
                ],
                estimated_hours=20,
                prerequisites=["beginner_path"]
            ),
            
            "advanced_path": LearningPath(
                id="advanced_path",
                name="Advanced Programming",
                description="Learn advanced concepts and techniques",
                difficulty_progression=[
                    DifficultyLevel.ADVANCED,
                    DifficultyLevel.ADVANCED,
                    DifficultyLevel.EXPERT
                ],
                modules=[
                    "data_structures",
                    "algorithms",
                    "api_integration",
                    "project_architecture"
                ],
                estimated_hours=40,
                prerequisites=["intermediate_path"]
            ),
        }
    
    def create_user_profile(self, username: str) -> UserProfile:
        """Create new user profile"""
        profile = UserProfile(
            username=username,
            level=1,
            experience_points=0,
            total_points=0,
            streak_days=0,
            last_active_date=datetime.now(),
            achievements=[],
            statistics={
                'total_code_lines': 0,
                'total_functions': 0,
                'total_projects': 0,
                'total_errors_fixed': 0,
                'total_hints_used': 0,
                'favorite_language': 'japanese',
                'preferred_difficulty': 'beginner'
            },
            learning_path="beginner_path",
            preferred_language="japanese",
            avatar=self._generate_avatar()
        )
        
        self.user_profile = profile
        return profile
    
    def _generate_avatar(self) -> str:
        """Generate random avatar"""
        avatars = ["👤", "👨‍💻", "👩‍💻", "🧑‍💻", "👨‍🎓", "👩‍🎓", 
                   "🧑‍🎓", "👨‍🔬", "👩‍🔬", "🧑‍🔬", "👨‍🎨", "👩‍🎨", "🧑‍🎨"]
        return random.choice(avatars)
    
    def track_activity(self, activity_type: str, value: Any = 1):
        """Track user activity and update progress"""
        if not self.user_profile:
            return
        
        # Update session statistics
        if activity_type == 'code_lines':
            self.current_session['code_lines'] += value
            self.user_profile.statistics['total_code_lines'] += value
        elif activity_type == 'functions_created':
            self.current_session['functions_created'] += value
            self.user_profile.statistics['total_functions'] += value
        elif activity_type == 'projects_completed':
            self.current_session['projects_completed'] += value
            self.user_profile.statistics['total_projects'] += value
        elif activity_type == 'errors_fixed':
            self.current_session['errors_fixed'] += value
            self.user_profile.statistics['total_errors_fixed'] += value
        elif activity_type == 'hints_used':
            self.current_session['hints_used'] += value
            self.user_profile.statistics['total_hints_used'] += value
        
        # Check for achievements
        self._check_achievements()
        
        # Update experience and level
        self._update_experience_and_level()
        
        # Update streak
        self._update_streak()
    
    def _check_achievements(self):
        """Check and unlock achievements"""
        total_lines = self.user_profile.statistics['total_code_lines']
        total_functions = self.user_profile.statistics['total_functions']
        total_projects = self.user_profile.statistics['total_projects']
        
        # Check code line achievements
        if total_lines >= 10 and "first_lines" not in self.user_profile.achievements:
            self._unlock_achievement("first_lines")
        
        if total_lines >= 1000 and "code_warrior" not in self.user_profile.achievements:
            self._unlock_achievement("code_warrior")
        
        if total_lines >= 5000 and "code_master" not in self.user_profile.achievements:
            self._unlock_achievement("code_master")
        
        # Check function achievements
        if total_functions >= 1 and "first_function" not in self.user_profile.achievements:
            self._unlock_achievement("first_function")
        
        if total_functions >= 50 and "function_expert" not in self.user_profile.achievements:
            self._unlock_achievement("function_expert")
        
        # Check project achievements
        if total_projects >= 1 and "first_project" not in self.user_profile.achievements:
            self._unlock_achievement("first_project")
        
        if total_projects >= 10 and "project_builder" not in self.user_profile.achievements:
            self._unlock_achievement("project_builder")
        
        # Update achievement progress
        self._update_achievement_progress()
    
    def _unlock_achievement(self, achievement_id: str):
        """Unlock an achievement"""
        if achievement_id in self.achievements:
            achievement = self.achievements[achievement_id]
            achievement.unlocked = True
            achievement.unlocked_at = datetime.now()
            achievement.progress = achievement.max_progress
            
            self.user_profile.achievements.append(achievement_id)
            self.user_profile.total_points += achievement.points
            
            return achievement
        return None
    
    def _update_achievement_progress(self):
        """Update progress for achievements"""
        total_lines = self.user_profile.statistics['total_code_lines']
        total_functions = self.user_profile.statistics['total_functions']
        total_projects = self.user_profile.statistics['total_projects']
        
        # Update progress for locked achievements
        for achievement_id, achievement in self.achievements.items():
            if not achievement.unlocked:
                if achievement.type == AchievementType.CODE_LINES:
                    if achievement_id == "code_warrior":
                        achievement.progress = min(100, (total_lines / 1000) * 100)
                    elif achievement_id == "code_master":
                        achievement.progress = min(100, (total_lines / 5000) * 100)
                
                elif achievement.type == AchievementType.FUNCTIONS:
                    if achievement_id == "function_expert":
                        achievement.progress = min(100, (total_functions / 50) * 100)
                
                elif achievement.type == AchievementType.PROJECTS:
                    if achievement_id == "project_builder":
                        achievement.progress = min(100, (total_projects / 10) * 100)
    
    def _update_experience_and_level(self):
        """Update user experience and level"""
        # Calculate experience from session activities
        session_exp = (
            self.current_session['code_lines'] * 1 +
            self.current_session['functions_created'] * 5 +
            self.current_session['projects_completed'] * 20 +
            self.current_session['errors_fixed'] * 3
        )
        
        self.user_profile.experience_points += session_exp
        
        # Calculate level (100 XP per level)
        new_level = (self.user_profile.experience_points // 100) + 1
        
        if new_level > self.user_profile.level:
            self.user_profile.level = new_level
            return True  # Leveled up
        
        return False
    
    def _update_streak(self):
        """Update daily streak"""
        today = datetime.now().date()
        last_active = self.user_profile.last_active_date.date()
        
        if today == last_active:
            return  # Already updated today
        
        if today == last_active + timedelta(days=1):
            self.user_profile.streak_days += 1
        elif today > last_active + timedelta(days=1):
            self.user_profile.streak_days = 1  # Reset streak
        
        self.user_profile.last_active_date = datetime.now()
        
        # Check streak achievements
        if self.user_profile.streak_days >= 7 and "week_streak" not in self.user_profile.achievements:
            self._unlock_achievement("week_streak")
        
        if self.user_profile.streak_days >= 30 and "month_streak" not in self.user_profile.achievements:
            self._unlock_achievement("month_streak")
    
    def complete_challenge(self, challenge_id: str, time_taken: int, hints_used: int = 0) -> bool:
        """Complete a challenge"""
        if challenge_id not in self.challenges:
            return False
        
        challenge = self.challenges[challenge_id]
        
        # Check if completed within time limit
        if time_taken > challenge.time_limit:
            return False
        
        # Calculate points (reduced for hints)
        points_earned = challenge.reward_points
        if hints_used > 0:
            points_earned = max(10, points_earned - (hints_used * 5))
        
        self.user_profile.total_points += points_earned
        self.user_profile.experience_points += points_earned // 2
        
        return True
    
    def get_leaderboard(self, category: str = "total_points") -> List[Tuple[str, int]]:
        """Get leaderboard (mock implementation)"""
        # In real implementation, this would query a database
        mock_users = [
            ("CodeMaster", 2500),
            ("ProgrammerPro", 2100),
            ("NinjaCoder", 1800),
            ("PythonWizard", 1500),
            ("BeginnerBob", 800),
        ]
        
        if category == "total_points":
            return mock_users
        elif category == "level":
            return [(name, points // 100) for name, points in mock_users]
        elif category == "streak":
            return [(name, random.randint(1, 30)) for name, _ in mock_users]
        
        return mock_users
    
    def get_recommendations(self) -> List[str]:
        """Get personalized recommendations"""
        recommendations = []
        
        if self.user_profile:
            level = self.user_profile.level
            preferred_lang = self.user_profile.preferred_language
            
            if level <= 3:
                recommendations.extend([
                    "Try the 'Hello World' challenge",
                    "Complete the 'Variable Magic' challenge",
                    "Watch the beginner tutorials"
                ])
            elif level <= 10:
                recommendations.extend([
                    "Create your first function",
                    "Try intermediate challenges",
                    "Explore control structures"
                ])
            else:
                recommendations.extend([
                    "Try advanced challenges",
                    "Help other users in forums",
                    "Create your own challenges"
                ])
        
        return recommendations

class GamificationGUI:
    """GUI for gamification system"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Nadesiko Python - Learning Adventure")
        self.root.geometry("1200x800")
        
        self.engine = GamificationEngine()
        self.current_user = None
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the gamification interface"""
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Top panel - User profile
        self.profile_frame = self._create_profile_panel()
        main_frame.pack(side=tk.TOP, fill=tk.X, pady=(0, 10))
        
        # Middle panel - Tabbed interface
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.create_achievements_tab()
        self.create_challenges_tab()
        self.create_progress_tab()
        self.create_leaderboard_tab()
        
        # Bottom panel - Quick actions
        self.actions_frame = self._create_actions_panel()
        main_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 0))
        
    def _create_profile_panel(self):
        """Create user profile panel"""
        frame = ttk.LabelFrame(self.root, text="👤 Profile", padding=10)
        
        # Avatar and username
        top_frame = ttk.Frame(frame)
        top_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.avatar_label = ttk.Label(top_frame, text="👤", font=("Arial", 24))
        self.avatar_label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.username_label = ttk.Label(top_frame, text="Guest", font=("Arial", 16, "bold"))
        self.username_label.pack(side=tk.LEFT)
        
        # Stats
        stats_frame = ttk.Frame(frame)
        stats_frame.pack(fill=tk.X)
        
        # Level and XP
        level_frame = ttk.Frame(stats_frame)
        level_frame.pack(fill=tk.X, pady=2)
        
        ttk.Label(level_frame, text="Level:").pack(side=tk.LEFT)
        self.level_label = ttk.Label(level_frame, text="1", font=("Arial", 12, "bold"))
        self.level_label.pack(side=tk.LEFT, padx=(10, 0))
        
        ttk.Label(level_frame, text="XP:").pack(side=tk.LEFT, padx=(20, 0))
        self.xp_label = ttk.Label(level_frame, text="0", font=("Arial", 12, "bold"))
        self.xp_label.pack(side=tk.LEFT, padx=(10, 0))
        
        # Points and streak
        points_frame = ttk.Frame(stats_frame)
        points_frame.pack(fill=tk.X, pady=2)
        
        ttk.Label(points_frame, text="Points:").pack(side=tk.LEFT)
        self.points_label = ttk.Label(points_frame, text="0", font=("Arial", 12, "bold"))
        self.points_label.pack(side=tk.LEFT, padx=(10, 0))
        
        ttk.Label(points_frame, text="Streak:").pack(side=tk.LEFT, padx=(20, 0))
        self.streak_label = ttk.Label(points_frame, text="0", font=("Arial", 12, "bold"))
        self.streak_label.pack(side=tk.LEFT, padx=(10, 0))
        
        # Login button
        login_btn = ttk.Button(frame, text="🔓 Login", command=self.show_login_dialog)
        login_btn.pack(pady=(10, 0))
        
        return frame
    
    def create_achievements_tab(self):
        """Create achievements tab"""
        tab_frame = ttk.Frame(self.notebook)
        self.notebook.add(tab_frame, text="🏆 Achievements")
        
        # Achievement categories
        categories_frame = ttk.Frame(tab_frame)
        categories_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create achievement display
        self.achievements_canvas = tk.Canvas(categories_frame, bg="white")
        self.achievements_canvas.pack(fill=tk.BOTH, expand=True)
        
        self.update_achievements_display()
        
    def create_challenges_tab(self):
        """Create challenges tab"""
        tab_frame = ttk.Frame(self.notebook)
        self.notebook.add(tab_frame, text="🎯 Challenges")
        
        # Challenge list
        challenges_frame = ttk.Frame(tab_frame)
        challenges_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Difficulty filter
        filter_frame = ttk.Frame(challenges_frame)
        filter_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(filter_frame, text="Difficulty:").pack(side=tk.LEFT)
        self.difficulty_var = tk.StringVar(value="all")
        difficulty_combo = ttk.Combobox(filter_frame, textvariable=self.difficulty_var,
                                     values=["all", "beginner", "intermediate", "advanced", "expert"])
        difficulty_combo.pack(side=tk.LEFT, padx=(10, 0))
        difficulty_combo.bind("<<ComboboxSelected>>", self.update_challenges_display)
        
        # Challenges list
        self.challenges_listbox = tk.Listbox(challenges_frame, font=("Arial", 10))
        self.challenges_listbox.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        # Challenge details
        details_frame = ttk.LabelFrame(challenges_frame, text="Challenge Details", padding=10)
        details_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.challenge_details = tk.Text(details_frame, height=8, wrap=tk.WORD, state=tk.DISABLED)
        self.challenge_details.pack(fill=tk.X)
        
        # Start challenge button
        start_btn = ttk.Button(details_frame, text="🚀 Start Challenge", command=self.start_challenge)
        start_btn.pack(pady=(10, 0))
        
        self.update_challenges_display()
        
    def create_progress_tab(self):
        """Create progress tracking tab"""
        tab_frame = ttk.Frame(self.notebook)
        self.notebook.add(tab_frame, text="📊 Progress")
        
        # Progress visualization
        progress_frame = ttk.Frame(tab_frame)
        progress_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create matplotlib figure for progress
        self.progress_fig, self.progress_axes = plt.subplots(2, 2, figsize=(10, 8))
        self.progress_fig.suptitle('Your Learning Progress', fontsize=14, fontweight='bold')
        
        # Embed in tkinter
        self.progress_canvas = FigureCanvasTkAgg(self.progress_fig, progress_frame)
        self.progress_canvas.draw()
        self.progress_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.update_progress_display()
        
    def create_leaderboard_tab(self):
        """Create leaderboard tab"""
        tab_frame = ttk.Frame(self.notebook)
        self.notebook.add(tab_frame, text="🏅 Leaderboard")
        
        # Leaderboard display
        leaderboard_frame = ttk.Frame(tab_frame)
        leaderboard_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Category selector
        category_frame = ttk.Frame(leaderboard_frame)
        category_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(category_frame, text="Category:").pack(side=tk.LEFT)
        self.leaderboard_category = tk.StringVar(value="total_points")
        category_combo = ttk.Combobox(category_frame, textvariable=self.leaderboard_category,
                                      values=["total_points", "level", "streak"])
        category_combo.pack(side=tk.LEFT, padx=(10, 0))
        category_combo.bind("<<ComboboxSelected>>", self.update_leaderboard_display)
        
        # Leaderboard list
        self.leaderboard_listbox = tk.Listbox(leaderboard_frame, font=("Arial", 12))
        self.leaderboard_listbox.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        self.update_leaderboard_display()
        
    def _create_actions_panel(self):
        """Create quick actions panel"""
        frame = ttk.LabelFrame(self.root, text="⚡ Quick Actions", padding=10)
        
        buttons = [
            ("🎮 Start Coding", self.start_coding_session),
            ("📚 View Tutorials", self.show_tutorials),
            ("🏆 View Achievements", self.show_achievements),
            ("🎯 Daily Challenge", self.show_daily_challenge),
            ("📊 Progress Report", self.show_progress_report),
            ("⚙️ Settings", self.show_settings),
        ]
        
        for i, (text, command) in enumerate(buttons):
            btn = ttk.Button(frame, text=text, command=command)
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5, sticky="ew")
        
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)
        
        return frame
    
    def update_achievements_display(self):
        """Update achievements display"""
        self.achievements_canvas.delete("all")
        
        if not self.engine.user_profile:
            self.achievements_canvas.create_text(400, 300, text="Please login to view achievements",
                                                 font=("Arial", 14), fill="gray")
            return
        
        # Display achievements in a grid
        x_start, y_start = 50, 50
        x_spacing, y_spacing = 120, 100
        
        for i, (achievement_id, achievement) in enumerate(self.engine.achievements.items()):
            x = x_start + (i % 5) * x_spacing
            y = y_start + (i // 5) * y_spacing
            
            # Achievement box
            color = "#90EE90" if achievement.unlocked else "#D0D0D0"
            self.achievements_canvas.create_rectangle(x-40, y-30, x+40, y+30, 
                                                   fill=color, outline="black", width=2)
            
            # Badge icon
            self.achievements_canvas.create_text(x, y-10, text=achievement.badge_icon, 
                                                 font=("Arial", 20))
            
            # Achievement name
            self.achievements_canvas.create_text(x, y+10, text=achievement.name, 
                                                 font=("Arial", 10, "bold"))
            
            # Points
            self.achievements_canvas.create_text(x, y+25, text=f"{achievement.points} pts", 
                                                 font=("Arial", 8))
    
    def update_challenges_display(self, event=None):
        """Update challenges display based on filter"""
        self.challenges_listbox.delete(0, tk.END)
        
        difficulty_filter = self.difficulty_var.get()
        
        for challenge_id, challenge in self.engine.challenges.items():
            if difficulty_filter == "all" or challenge.difficulty.value == difficulty_filter:
                display_text = f"{challenge.title} ({challenge.difficulty.value.title()})"
                self.challenges_listbox.insert(tk.END, display_text)
    
    def update_progress_display(self):
        """Update progress visualization"""
        if not self.engine.user_profile:
            return
        
        # Clear previous plots
        for ax in self.progress_axes.flat:
            ax.clear()
        
        # Mock data for visualization
        stats = self.engine.user_profile.statistics
        
        # XP over time
        self.progress_axes[0, 0].plot(range(7), [10, 25, 40, 65, 90, 120, 150], 'o-')
        self.progress_axes[0, 0].set_title('XP Progress')
        self.progress_axes[0, 0].set_ylabel('XP')
        
        # Achievement categories
        categories = ['Code', 'Functions', 'Projects', 'Debugging']
        values = [
            stats.get('total_code_lines', 0) // 100,
            stats.get('total_functions', 0),
            stats.get('total_projects', 0),
            stats.get('total_errors_fixed', 0)
        ]
        
        self.progress_axes[0, 1].bar(categories, values, color=['skyblue', 'lightgreen', 'salmon', 'gold'])
        self.progress_axes[0, 1].set_title('Achievement Categories')
        self.progress_axes[0, 1].set_ylabel('Count')
        
        # Learning path progress
        path_progress = [20, 45, 70, 85]  # Mock data
        self.progress_axes[1, 0].plot(range(4), path_progress, 'o-')
        self.progress_axes[1, 0].set_title('Learning Path Progress')
        self.progress_axes[1, 0].set_ylabel('Completion %')
        
        # Activity heatmap
        activity_data = [[random.randint(0, 10) for _ in range(7)] for _ in range(4)]  # Mock data
        self.progress_axes[1, 1].imshow(activity_data, cmap='YlOrRd', aspect='auto')
        self.progress_axes[1, 1].set_title('Activity Heatmap')
        
        self.progress_fig.tight_layout()
        self.progress_canvas.draw()
    
    def update_leaderboard_display(self, event=None):
        """Update leaderboard display"""
        self.leaderboard_listbox.delete(0, tk.END)
        
        category = self.leaderboard_category.get()
        leaderboard = self.engine.get_leaderboard(category)
        
        for i, (username, score) in enumerate(leaderboard):
            display_text = f"{i+1}. {username}: {score}"
            self.leaderboard_listbox.insert(tk.END, display_text)
    
    def show_login_dialog(self):
        """Show login dialog"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Login")
        dialog.geometry("300x200")
        
        ttk.Label(dialog, text="Username:").pack(pady=10)
        username_entry = ttk.Entry(dialog)
        username_entry.pack(pady=5)
        
        def login():
            username = username_entry.get().strip()
            if username:
                self.current_user = self.engine.create_user_profile(username)
                self.update_profile_display()
                dialog.destroy()
        
        ttk.Button(dialog, text="Login", command=login).pack(pady=20)
    
    def update_profile_display(self):
        """Update profile display"""
        if self.engine.user_profile:
            profile = self.engine.user_profile
            self.avatar_label.config(text=profile.avatar)
            self.username_label.config(text=profile.username)
            self.level_label.config(text=str(profile.level))
            self.xp_label.config(text=str(profile.experience_points))
            self.points_label.config(text=str(profile.total_points))
            self.streak_label.config(text=str(profile.streak_days))
    
    def start_coding_session(self):
        """Start coding session"""
        messagebox.showinfo("Coding Session", "Starting your coding session! Track your progress and earn points!")
    
    def show_tutorials(self):
        """Show tutorials"""
        messagebox.showinfo("Tutorials", "Interactive tutorials coming soon!")
    
    def show_achievements(self):
        """Show achievements"""
        self.notebook.select(0)  # Select achievements tab
    
    def show_daily_challenge(self):
        """Show daily challenge"""
        messagebox.showinfo("Daily Challenge", "Today's challenge: Create a calculator program!")
    
    def show_progress_report(self):
        """Show progress report"""
        if self.engine.user_profile:
            stats = self.engine.user_profile.statistics
            report = f"""
            📊 Your Progress Report
            
            Total Code Lines: {stats.get('total_code_lines', 0)}
            Total Functions: {stats.get('total_functions', 0)}
            Total Projects: {stats.get('total_projects', 0)}
            Errors Fixed: {stats.get('total_errors_fixed', 0)}
            Current Level: {self.engine.user_profile.level}
            Current Streak: {self.engine.user_profile.streak_days} days
            """
            messagebox.showinfo("Progress Report", report)
        else:
            messagebox.showinfo("Progress Report", "Please login to view your progress!")
    
    def show_settings(self):
        """Show settings"""
        messagebox.showinfo("Settings", "Settings panel coming soon!")
    
    def start_challenge(self):
        """Start selected challenge"""
        selection = self.challenges_listbox.curselection()
        if selection:
            index = selection[0]
            challenge_id = list(self.engine.challenges.keys())[index]
            challenge = self.engine.challenges[challenge_id]
            
            messagebox.showinfo("Challenge Started", 
                              f"Started: {challenge.title}\n\n{challenge.description}")
    
    def run(self):
        """Run the GUI"""
        self.root.mainloop()

# Usage example
def main():
    app = GamificationGUI()
    app.run()

if __name__ == "__main__":
    main()
