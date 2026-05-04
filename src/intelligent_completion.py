"""
Intelligent Code Completion and Suggestions - World-changing AI assistance
"""

import re
import json
import numpy as np
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass
from collections import defaultdict
import difflib

@dataclass
class CompletionSuggestion:
    text: str
    type: str  # 'keyword', 'variable', 'function', 'pattern'
    confidence: float
    description: str
    priority: int

@dataclass
class CodeContext:
    current_line: str
    previous_lines: List[str]
    variables: Dict[str, Any]
    functions: Dict[str, Any]
    indent_level: int
    language_mode: str  # 'japanese', 'english', 'auto'

class IntelligentCompletionEngine:
    """AI-powered code completion engine"""
    
    def __init__(self):
        self.japanese_keywords = {
            'variables': ['は', 'とは', 'に代入', 'を代入'],
            'operators': ['と', 'から', 'を掛ける', 'で割る', '以上', '以下', 'より大きい', 'より小さい', 'と等しい', 'と異なる'],
            'control': ['もし', 'ならば', 'そうでなければ', '違えば', '繰り返す', 'の間'],
            'functions': ['●', 'を返す', 'を戻る', 'を表示', 'を表示する', 'を読む', 'を読み込む'],
            'builtins': ['文字数', '左から', '右から', '大文字', '小文字', '絶対値', '平方根', '円周率'],
        }
        
        self.english_keywords = {
            'variables': ['is', 'are', 'let', 'set', 'assign'],
            'operators': ['plus', 'minus', 'times', 'multiplied by', 'divided by', 'greater than', 'less than', 'equal to'],
            'control': ['if', 'else', 'otherwise', 'repeat', 'while', 'for'],
            'functions': ['function', 'return', 'show', 'print', 'display', 'read', 'input'],
            'builtins': ['length', 'left', 'right', 'upper', 'lower', 'abs', 'sqrt', 'pi'],
        }
        
        self.common_patterns = [
            # Japanese patterns
            (r'(\w+)(は|とは)$', 'variable_assignment'),
            (r'(\w+)(と)(\w+)(を足す|を掛ける|を引く|で割る)$', 'calculation'),
            (r'もし(.+)(ならば)$', 'conditional_start'),
            (r'(\d+)(回|回だけ)(繰り返す)$', 'loop_start'),
            (r'●(\w+)(（|\\()$', 'function_definition'),
            
            # English patterns
            (r'(\w+)(\s+is\s+|\s+are\s+)$', 'variable_assignment'),
            (r'(\w+)(\s+plus\s+|\s+minus\s+|\s+times\s+|\s+divided by\s+)(\w+)$', 'calculation'),
            (r'if\s+(.+)$', 'conditional_start'),
            (r'repeat\s+(\d+)\s+times$', 'loop_start'),
            (r'function\s+(\w+)(\\(|\\()$', 'function_definition'),
        ]
        
        self.learning_data = defaultdict(list)
        self.user_preferences = {}
        
    def get_completions(self, context: CodeContext) -> List[CompletionSuggestion]:
        """Get intelligent completion suggestions"""
        suggestions = []
        
        # Pattern-based completions
        pattern_suggestions = self._get_pattern_completions(context)
        suggestions.extend(pattern_suggestions)
        
        # Keyword completions
        keyword_suggestions = self._get_keyword_completions(context)
        suggestions.extend(keyword_suggestions)
        
        # Variable completions
        variable_suggestions = self._get_variable_completions(context)
        suggestions.extend(variable_suggestions)
        
        # Function completions
        function_suggestions = self._get_function_completions(context)
        suggestions.extend(function_suggestions)
        
        # AI-powered completions based on learning
        ai_suggestions = self._get_ai_completions(context)
        suggestions.extend(ai_suggestions)
        
        # Sort by priority and confidence
        suggestions.sort(key=lambda x: (x.priority, -x.confidence))
        
        # Remove duplicates and limit results
        unique_suggestions = []
        seen = set()
        
        for suggestion in suggestions:
            if suggestion.text not in seen:
                unique_suggestions.append(suggestion)
                seen.add(suggestion.text)
        
        return unique_suggestions[:10]  # Top 10 suggestions
    
    def _get_pattern_completions(self, context: CodeContext) -> List[CompletionSuggestion]:
        """Get pattern-based completions"""
        suggestions = []
        current_text = context.current_line.strip()
        
        for pattern, pattern_type in self.common_patterns:
            if re.search(pattern, current_text):
                completions = self._get_pattern_completion(pattern_type, context)
                suggestions.extend(completions)
        
        return suggestions
    
    def _get_pattern_completion(self, pattern_type: str, context: CodeContext) -> List[CompletionSuggestion]:
        """Get completions for specific pattern type"""
        completions = []
        
        if pattern_type == 'variable_assignment':
            if context.language_mode in ['japanese', 'auto']:
                completions.extend([
                    CompletionSuggestion('は10', 'pattern', 0.9, 'Assign value 10', 1),
                    CompletionSuggestion('とは20', 'pattern', 0.9, 'Assign value 20', 1),
                    CompletionSuggestion('に30を代入', 'pattern', 0.8, 'Assign value 30', 1),
                ])
            
            if context.language_mode in ['english', 'auto']:
                completions.extend([
                    CompletionSuggestion(' is 10', 'pattern', 0.9, 'Assign value 10', 1),
                    CompletionSuggestion(' are 20', 'pattern', 0.9, 'Assign value 20', 1),
                    CompletionSuggestion(' = 30', 'pattern', 0.8, 'Assign value 30', 1),
                ])
        
        elif pattern_type == 'calculation':
            if context.language_mode in ['japanese', 'auto']:
                completions.extend([
                    CompletionSuggestion('とBを足す', 'pattern', 0.95, 'Add with B', 1),
                    CompletionSuggestion('からBを引く', 'pattern', 0.95, 'Subtract B', 1),
                    CompletionSuggestion('にBを掛ける', 'pattern', 0.95, 'Multiply by B', 1),
                    CompletionSuggestion('をBで割る', 'pattern', 0.95, 'Divide by B', 1),
                ])
            
            if context.language_mode in ['english', 'auto']:
                completions.extend([
                    CompletionSuggestion(' plus B', 'pattern', 0.95, 'Add with B', 1),
                    CompletionSuggestion(' minus B', 'pattern', 0.95, 'Subtract B', 1),
                    CompletionSuggestion(' times B', 'pattern', 0.95, 'Multiply by B', 1),
                    CompletionSuggestion(' divided by B', 'pattern', 0.95, 'Divide by B', 1),
                ])
        
        elif pattern_type == 'conditional_start':
            if context.language_mode in ['japanese', 'auto']:
                completions.extend([
                    CompletionSuggestion('ならば', 'pattern', 0.9, 'Complete if statement', 1),
                    CompletionSuggestion('そうでなければ', 'pattern', 0.8, 'Else clause', 2),
                    CompletionSuggestion('違えば', 'pattern', 0.8, 'Alternative else', 2),
                ])
            
            if context.language_mode in ['english', 'auto']:
                completions.extend([
                    CompletionSuggestion(' then', 'pattern', 0.9, 'Complete if statement', 1),
                    CompletionSuggestion(' else', 'pattern', 0.8, 'Else clause', 2),
                    CompletionSuggestion(' otherwise', 'pattern', 0.8, 'Alternative else', 2),
                ])
        
        elif pattern_type == 'loop_start':
            if context.language_mode in ['japanese', 'auto']:
                completions.extend([
                    CompletionSuggestion('回繰り返す', 'pattern', 0.95, 'Complete loop', 1),
                ])
            
            if context.language_mode in ['english', 'auto']:
                completions.extend([
                    CompletionSuggestion(' times', 'pattern', 0.95, 'Complete loop', 1),
                ])
        
        elif pattern_type == 'function_definition':
            if context.language_mode in ['japanese', 'auto']:
                completions.extend([
                    CompletionSuggestion('（引数）', 'pattern', 0.9, 'Function parameters', 1),
                    CompletionSuggestion('を返す', 'pattern', 0.8, 'Return statement', 2),
                ])
            
            if context.language_mode in ['english', 'auto']:
                completions.extend([
                    CompletionSuggestion('(param)', 'pattern', 0.9, 'Function parameters', 1),
                    CompletionSuggestion(' return', 'pattern', 0.8, 'Return statement', 2),
                ])
        
        return completions
    
    def _get_keyword_completions(self, context: CodeContext) -> List[CompletionSuggestion]:
        """Get keyword completions"""
        suggestions = []
        current_text = context.current_line.strip()
        
        # Determine language
        if context.language_mode == 'auto':
            if any(char in current_text for char in 'はをにでと'):
                keywords = self.japanese_keywords
            else:
                keywords = self.english_keywords
        elif context.language_mode == 'japanese':
            keywords = self.japanese_keywords
        else:
            keywords = self.english_keywords
        
        # Find matching keywords
        for category, keyword_list in keywords.items():
            for keyword in keyword_list:
                if keyword.startswith(current_text) and len(keyword) > len(current_text):
                    suggestions.append(CompletionSuggestion(
                        text=keyword,
                        type='keyword',
                        confidence=0.8,
                        description=f'{category} keyword',
                        priority=2
                    ))
        
        return suggestions
    
    def _get_variable_completions(self, context: CodeContext) -> List[CompletionSuggestion]:
        """Get variable completions"""
        suggestions = []
        current_text = context.current_line.strip()
        
        for var_name in context.variables.keys():
            if var_name.startswith(current_text) and len(var_name) > len(current_text):
                suggestions.append(CompletionSuggestion(
                    text=var_name,
                    type='variable',
                    confidence=0.9,
                    description=f'Variable: {var_name}',
                    priority=1
                ))
        
        return suggestions
    
    def _get_function_completions(self, context: CodeContext) -> List[CompletionSuggestion]:
        """Get function completions"""
        suggestions = []
        current_text = context.current_line.strip()
        
        for func_name in context.functions.keys():
            if func_name.startswith(current_text) and len(func_name) > len(current_text):
                suggestions.append(CompletionSuggestion(
                    text=func_name,
                    type='function',
                    confidence=0.85,
                    description=f'Function: {func_name}',
                    priority=1
                ))
        
        return suggestions
    
    def _get_ai_completions(self, context: CodeContext) -> List[CompletionSuggestion]:
        """Get AI-powered completions based on learning"""
        suggestions = []
        
        # Analyze user's coding patterns
        pattern_key = self._get_pattern_key(context)
        
        if pattern_key in self.learning_data:
            learned_completions = self.learning_data[pattern_key]
            
            for completion_data in learned_completions:
                suggestions.append(CompletionSuggestion(
                    text=completion_data['text'],
                    type='ai_suggestion',
                    confidence=completion_data['confidence'],
                    description='AI learned suggestion',
                    priority=3
                ))
        
        return suggestions
    
    def _get_pattern_key(self, context: CodeContext) -> str:
        """Generate pattern key for learning"""
        # Simple pattern extraction - in real implementation, this would be more sophisticated
        key_words = []
        
        for line in context.previous_lines[-3:]:  # Last 3 lines
            words = re.findall(r'\w+', line)
            key_words.extend(words[:3])  # First 3 words per line
        
        return '_'.join(key_words[:5])  # Limit pattern size
    
    def learn_from_completion(self, context: CodeContext, selected_completion: str):
        """Learn from user's completion selection"""
        pattern_key = self._get_pattern_key(context)
        
        # Add to learning data
        self.learning_data[pattern_key].append({
            'text': selected_completion,
            'confidence': 0.7,  # Initial confidence
            'timestamp': __import__('datetime').datetime.now()
        })
        
        # Limit learning data size
        if len(self.learning_data[pattern_key]) > 100:
            self.learning_data[pattern_key] = self.learning_data[pattern_key][-50:]
    
    def update_user_preferences(self, preferences: Dict[str, Any]):
        """Update user preferences for better suggestions"""
        self.user_preferences.update(preferences)
    
    def get_smart_suggestions(self, context: CodeContext) -> List[CompletionSuggestion]:
        """Get smart suggestions based on context analysis"""
        suggestions = []
        
        # Analyze code structure
        if self._is_in_function(context):
            suggestions.extend(self._get_function_suggestions(context))
        
        if self._is_in_loop(context):
            suggestions.extend(self._get_loop_suggestions(context))
        
        if self._is_error_recovery(context):
            suggestions.extend(self._get_error_recovery_suggestions(context))
        
        return suggestions
    
    def _is_in_function(self, context: CodeContext) -> bool:
        """Check if cursor is inside function"""
        for line in reversed(context.previous_lines):
            if '●' in line or 'function' in line:
                return True
            if 'ここ' in line or 'koko' in line or 'return' in line:
                return False
        return False
    
    def _is_in_loop(self, context: CodeContext) -> bool:
        """Check if cursor is inside loop"""
        for line in reversed(context.previous_lines):
            if '繰り返す' in line or 'repeat' in line:
                return True
            if 'ここ' in line or 'koko' in line:
                return False
        return False
    
    def _is_error_recovery(self, context: CodeContext) -> bool:
        """Check if this might be error recovery"""
        # Check for common error patterns
        error_indicators = ['エラー', 'error', 'except', 'try']
        return any(indicator in context.current_line.lower() for indicator in error_indicators)
    
    def _get_function_suggestions(self, context: CodeContext) -> List[CompletionSuggestion]:
        """Get function-specific suggestions"""
        suggestions = []
        
        if context.language_mode in ['japanese', 'auto']:
            suggestions.extend([
                CompletionSuggestion('を返す', 'function', 0.9, 'Return value', 1),
                CompletionSuggestion('ここまで', 'function', 0.8, 'End function', 2),
            ])
        
        if context.language_mode in ['english', 'auto']:
            suggestions.extend([
                CompletionSuggestion(' return', 'function', 0.9, 'Return value', 1),
                CompletionSuggestion(' koko', 'function', 0.8, 'End function', 2),
            ])
        
        return suggestions
    
    def _get_loop_suggestions(self, context: CodeContext) -> List[CompletionSuggestion]:
        """Get loop-specific suggestions"""
        suggestions = []
        
        if context.language_mode in ['japanese', 'auto']:
            suggestions.extend([
                CompletionSuggestion('ここまで', 'loop', 0.9, 'End loop', 1),
                CompletionSuggestion('抜ける', 'loop', 0.7, 'Break loop', 2),
            ])
        
        if context.language_mode in ['english', 'auto']:
            suggestions.extend([
                CompletionSuggestion(' koko', 'loop', 0.9, 'End loop', 1),
                CompletionSuggestion(' break', 'loop', 0.7, 'Break loop', 2),
            ])
        
        return suggestions
    
    def _get_error_recovery_suggestions(self, context: CodeContext) -> List[CompletionSuggestion]:
        """Get error recovery suggestions"""
        suggestions = []
        
        suggestions.extend([
            CompletionSuggestion('try:', 'error_recovery', 0.8, 'Try block', 1),
            CompletionSuggestion('except:', 'error_recovery', 0.8, 'Except block', 1),
            CompletionSuggestion('finally:', 'error_recovery', 0.7, 'Finally block', 2),
        ])
        
        return suggestions

class CompletionUI:
    """User interface for code completion"""
    
    def __init__(self, engine: IntelligentCompletionEngine):
        self.engine = engine
        self.completions = []
        self.selected_index = 0
        
    def show_completions(self, suggestions: List[CompletionSuggestion]) -> str:
        """Show completion suggestions to user"""
        if not suggestions:
            return ""
        
        # Format suggestions for display
        formatted = []
        for i, suggestion in enumerate(suggestions[:5]):  # Top 5
            icon = self._get_icon(suggestion.type)
            formatted.append(f"{i+1}. {icon} {suggestion.text} - {suggestion.description}")
        
        return "\n".join(formatted)
    
    def _get_icon(self, suggestion_type: str) -> str:
        """Get icon for suggestion type"""
        icons = {
            'keyword': '🔑',
            'variable': '📦',
            'function': '⚡',
            'pattern': '🎯',
            'ai_suggestion': '🤖',
            'error_recovery': '🔧',
            'loop': '🔄',
            'function': '📋'
        }
        return icons.get(suggestion_type, '💡')
    
    def select_completion(self, index: int) -> Optional[CompletionSuggestion]:
        """Select completion by index"""
        if 0 <= index < len(self.completions):
            return self.completions[index]
        return None

# Usage example
def main():
    engine = IntelligentCompletionEngine()
    ui = CompletionUI(engine)
    
    # Example context
    context = CodeContext(
        current_line="A",
        previous_lines=["Bは10", "Cは20"],
        variables={"B": 10, "C": 20},
        functions={},
        indent_level=0,
        language_mode="japanese"
    )
    
    # Get completions
    suggestions = engine.get_completions(context)
    
    # Show completions
    completion_display = ui.show_completions(suggestions)
    print(completion_display)
    
    # Simulate user selection
    if suggestions:
        selected = ui.select_completion(0)
        engine.learn_from_completion(context, selected.text)
        print(f"Selected: {selected.text}")

if __name__ == "__main__":
    main()
