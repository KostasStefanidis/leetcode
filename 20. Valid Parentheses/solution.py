class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_map = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        num_char_even = False if (len(s) % 2 == 1) else True
        if not num_char_even:
            return False
        
        open_bracket_list = []
        
        for char in s:
            if char in bracket_map.values():
                open_bracket_list.append(char)
            else:
                if len(open_bracket_list) == 0 or bracket_map.get(char) != open_bracket_list.pop():
                    return False
        
        return len(open_bracket_list) == 0
                