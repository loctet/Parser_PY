import re

class PatternChecker:
    @staticmethod
    def follows_pattern(input_string):
        input_string = input_string.strip()
        if input_string == '':
            return True
        
        pattern = r'^(\s*([a-zA-Z_]\w*|\w+\[\s*-?\d+\s*\])\s*:=\s*[^&|]+(&\s*([a-zA-Z_]\w*|\w+\[\s*-?\d+\s*\])\s*:=\s*[^&|]+)*)$'
        return bool(re.match(pattern, input_string))
