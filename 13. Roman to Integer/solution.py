class Solution:
    def __init__(self):
        self.roman_mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def romanToInt(self, s: str) -> int:
        sum: int = 0
        i: int = 0
        while (i < len(s)):
            current_char = s[i]
            num: int = self.roman_mapping.get(current_char)
            
            if i != len(s)-1:
                # if the character is not the last get the next one also
                next_char = s[i+1]
            
                if current_char == 'I' and next_char == 'V':
                    num = 4
                    i = i + 1
                if current_char == 'I' and next_char == 'X':
                    num = 9
                    i = i + 1
                    
                if current_char == 'X' and next_char == 'L':
                    num = 40
                    i = i + 1
                if current_char == 'X' and next_char == 'C':
                    num = 90
                    i = i + 1
                                
                if current_char == 'C' and next_char == 'D':
                    num = 400
                    i = i + 1
                if current_char == 'C' and next_char == 'M':
                    num = 900
                    i = i + 1
            
            sum = sum + num
            i = i + 1
        
        return sum  