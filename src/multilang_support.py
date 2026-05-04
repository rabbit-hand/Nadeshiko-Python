"""
Multi-Language Support - World-changing global programming language support
"""

import re
import json
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass
from enum import Enum

class Language(Enum):
    JAPANESE = "ja"
    ENGLISH = "en"

@dataclass
class LanguagePattern:
    language: Language
    patterns: Dict[str, str]
    keywords: Dict[str, List[str]]
    examples: Dict[str, str]
    direction: str  # 'ltr' or 'rtl'

class MultiLanguageParser:
    """World-changing multi-language natural programming parser"""
    
    def __init__(self):
        self.language_patterns = self._initialize_language_patterns()
        self.current_language = Language.JAPANESE
        self.auto_detect = True
        
    def _initialize_language_patterns(self) -> Dict[Language, LanguagePattern]:
        """Initialize patterns for Japanese and English only"""
        return {
            Language.JAPANESE: LanguagePattern(
                language=Language.JAPANESE,
                patterns={
                    'variable': r'(\w+)(は|とは|に代入|を代入)(.+)',
                    'calculation': r'(.+)(と|から|に|を)(.+)(足す|引く|掛ける|割る)',
                    'condition': r'もし(.+)(ならば|なら|だったら)',
                    'loop': r'(\d+)(回|回だけ)(繰り返す)',
                    'function': r'●(\w+)[（(](.+)[)）]',
                    'display': r'「(.+)(を表示|を表示する|を出力)',
                },
                keywords={
                    'variables': ['は', 'とは', 'に代入', 'を代入'],
                    'operators': ['と', 'から', 'に', 'を', '足す', '引く', '掛ける', '割る'],
                    'control': ['もし', 'ならば', 'そうでなければ', '違えば', '繰り返す'],
                    'functions': ['●', 'を返す', 'を戻る', 'を表示', 'を表示する'],
                    'builtins': ['文字数', '左から', '右から', '大文字', '小文字'],
                },
                examples={
                    'variable': 'Aは10',
                    'calculation': 'AとBを足す',
                    'condition': 'もしAが10以上ならば',
                    'loop': '5回繰り返す',
                    'function': '●足し算（AとB）',
                    'display': '「こんにちは」を表示',
                },
                direction='ltr'
            ),
            
            Language.ENGLISH: LanguagePattern(
                language=Language.ENGLISH,
                patterns={
                    'variable': r'(\w+)(\s+is\s+|\s+are\s+|\s*=\s*)(.+)',
                    'calculation': r'(.+)(\s+plus\s+|\s+minus\s+|\s+times\s+|\s+multiplied by\s+|\s+divided by\s+)(.+)',
                    'condition': r'if\s+(.+)(\s+then\s*)?',
                    'loop': r'repeat\s+(\d+)\s+times',
                    'function': r'function\s+(\w+)\s*[(](.+)[)]',
                    'display': r'(show|print|display)\s+["\'](.+)["\']',
                },
                keywords={
                    'variables': ['is', 'are', '=', 'let', 'set'],
                    'operators': ['plus', 'minus', 'times', 'multiplied by', 'divided by'],
                    'control': ['if', 'else', 'otherwise', 'repeat', 'while', 'for'],
                    'functions': ['function', 'return', 'show', 'print', 'display'],
                    'builtins': ['length', 'left', 'right', 'upper', 'lower'],
                },
                examples={
                    'variable': 'A is 10',
                    'calculation': 'A plus B',
                    'condition': 'if A is greater than 10',
                    'loop': 'repeat 5 times',
                    'function': 'function add(A and B)',
                    'display': 'show "Hello"',
                },
                direction='ltr'
            ),
        }
    
    def detect_language(self, text: str) -> Language:
        """Detect the programming language from text"""
        language_scores = {}
        
        for language, pattern in self.language_patterns.items():
            score = 0
            
            # Check keywords
            for category, keywords in pattern.keywords.items():
                for keyword in keywords:
                    if keyword in text:
                        score += 1
            
            # Check patterns
            for pattern_type, regex in pattern.patterns.items():
                if re.search(regex, text):
                    score += 2
            
            language_scores[language] = score
        
        # Return language with highest score
        if language_scores:
            return max(language_scores, key=language_scores.get)
        
        return Language.JAPANESE  # Default
    
    def parse_code(self, code: str, target_language: Language = None) -> Dict[str, Any]:
        """Parse code in specified or detected language"""
        if target_language is None:
            target_language = self.detect_language(code) if self.auto_detect else self.current_language
        
        if target_language not in self.language_patterns:
            raise ValueError(f"Language {target_language} not supported")
        
        pattern = self.language_patterns[target_language]
        
        # Parse line by line
        parsed_lines = []
        lines = code.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            parsed_line = self._parse_line(line, pattern, line_num)
            parsed_lines.append(parsed_line)
        
        return {
            'language': target_language,
            'pattern': pattern,
            'parsed_lines': parsed_lines,
            'original_code': code,
            'direction': pattern.direction
        }
    
    def _parse_line(self, line: str, pattern: LanguagePattern, line_num: int) -> Dict[str, Any]:
        """Parse a single line of code"""
        result = {
            'line_number': line_num,
            'original': line,
            'type': 'unknown',
            'components': {},
            'python_code': None
        }
        
        # Try each pattern
        for pattern_type, regex in pattern.patterns.items():
            match = re.search(regex, line)
            if match:
                result['type'] = pattern_type
                result['components'] = match.groupdict()
                result['python_code'] = self._convert_to_python(pattern_type, match, pattern.language)
                break
        
        return result
    
    def _convert_to_python(self, pattern_type: str, match, language: Language) -> str:
        """Convert parsed pattern to Python code"""
        conversions = {
            'variable': self._convert_variable,
            'calculation': self._convert_calculation,
            'condition': self._convert_condition,
            'loop': self._convert_loop,
            'function': self._convert_function,
            'display': self._convert_display,
        }
        
        converter = conversions.get(pattern_type, lambda x, y: f"# Unknown pattern: {pattern_type}")
        return converter(match, language)
    
    def _convert_variable(self, match, language: Language) -> str:
        """Convert variable assignment to Python"""
        var_name = match.group(1)
        value = match.group(2).strip()
        
        # Try to evaluate the value
        try:
            # Simple evaluation for numeric values
            if value.replace('.', '').replace('-', '').isdigit():
                return f"{var_name} = {value}"
            else:
                return f"{var_name} = '{value}'"
        except:
            return f"{var_name} = '{value}'"
    
    def _convert_calculation(self, match, language: Language) -> str:
        """Convert calculation to Python"""
        left = match.group(1)
        operator = match.group(2)
        right = match.group(3)
        
        # Map language-specific operators to Python
        op_map = {
            # Japanese
            'と': '+', 'から': '-', 'に': '*', 'を': '/', '足す': '+', '引く': '-', '掛ける': '*', '割る': '/',
            # English
            'plus': '+', 'minus': '-', 'times': '*', 'multiplied by': '*', 'divided by': '/',
        }
        
        python_op = op_map.get(operator, '+')
        return f"result = {left} {python_op} {right}"
    
    def _convert_condition(self, match, language: Language) -> str:
        """Convert condition to Python"""
        condition = match.group(1)
        return f"if {condition}:"
    
    def _convert_loop(self, match, language: Language) -> str:
        """Convert loop to Python"""
        count = match.group(1)
        return f"for _ in range({count}):"
    
    def _convert_function(self, match, language: Language) -> str:
        """Convert function definition to Python"""
        func_name = match.group(1)
        params = match.group(2)
        return f"def {func_name}({params}):"
    
    def _convert_display(self, match, language: Language) -> str:
        """Convert display to Python"""
        content = match.group(1)
        return f"print('{content}')"
    
    def get_supported_languages(self) -> List[Dict[str, Any]]:
        """Get list of supported languages with examples"""
        languages = []
        
        for lang, pattern in self.language_patterns.items():
            languages.append({
                'code': lang.value,
                'name': lang.name.title(),
                'direction': pattern.direction,
                'examples': pattern.examples,
                'keywords_count': sum(len(kw) for kw in pattern.keywords.values())
            })
        
        return languages
    
    def translate_code(self, code: str, from_lang: Language, to_lang: Language) -> str:
        """Translate code from one language to another"""
        # Parse source code
        parsed = self.parse_code(code, from_lang)
        
        # Convert to target language
        target_pattern = self.language_patterns[to_lang]
        translated_lines = []
        
        for parsed_line in parsed['parsed_lines']:
            if parsed_line['type'] != 'unknown':
                # Use target language examples for translation
                example_key = parsed_line['type']
                if example_key in target_pattern.examples:
                    translated_lines.append(target_pattern.examples[example_key])
                else:
                    translated_lines.append(parsed_line['original'])
            else:
                translated_lines.append(parsed_line['original'])
        
        return '\n'.join(translated_lines)
    
    def get_language_info(self, language: Language) -> Dict[str, Any]:
        """Get detailed information about a language"""
        if language not in self.language_patterns:
            return {}
        
        pattern = self.language_patterns[language]
        return {
            'language': language.value,
            'name': language.name.title(),
            'direction': pattern.direction,
            'patterns': pattern.patterns,
            'keywords': pattern.keywords,
            'examples': pattern.examples,
            'total_keywords': sum(len(kw) for kw in pattern.keywords.values())
        }
    
    def set_language(self, language: Language):
        """Set the current programming language"""
        self.current_language = language
    
    def enable_auto_detect(self, enabled: bool = True):
        """Enable or disable automatic language detection"""
        self.auto_detect = enabled
    
    def create_multilang_program(self, code_blocks: List[Tuple[str, Language]]) -> str:
        """Create a multi-language program from code blocks"""
        program_parts = []
        
        for i, (code, lang) in enumerate(code_blocks):
            parsed = self.parse_code(code, lang)
            program_parts.append(f"# Language: {lang.name.title()}")
            program_parts.extend([line['python_code'] for line in parsed['parsed_lines'] if line['python_code']])
            program_parts.append("")  # Empty line between languages
        
        return '\n'.join(program_parts)

# Usage example
def main():
    parser = MultiLanguageParser()
    
    # Example code in different languages
    codes = [
        ("Aは10", Language.JAPANESE),
        ("B is 20", Language.ENGLISH),
        ("C加30", Language.CHINESE),
        ("D más 40", Language.SPANISH),
        ("E est 50", Language.FRENCH),
    ]
    
    print("=== Multi-Language Programming Demo ===")
    
    for code, lang in codes:
        print(f"\n--- {lang.name.title()} ---")
        print(f"Original: {code}")
        
        # Parse and convert
        parsed = parser.parse_code(code, lang)
        for line in parsed['parsed_lines']:
            if line['python_code']:
                print(f"Python: {line['python_code']}")
    
    # Create multi-language program
    print("\n=== Multi-Language Program ===")
    multilang_code = parser.create_multilang_program(codes)
    print(multilang_code)
    
    # Get supported languages
    print("\n=== Supported Languages ===")
    for lang_info in parser.get_supported_languages():
        print(f"{lang_info['name']} ({lang_info['code']}): {lang_info['keywords_count']} keywords")

if __name__ == "__main__":
    main()
