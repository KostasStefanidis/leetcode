from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(reversed(digits))
        
        if len(digits) == 1:
            if digits[0] + 1 > 9:
                digits[0] = 0
                digits.append(1)
            else:
                digits[0] = digits[0] + 1
            
            return list(reversed(digits))
        
        i = 1
        overflow = True
        while overflow:
            if digits[i-1] + 1 > 9:
                digits[i-1] = 0
                overflow = True
            else:
                digits[i-1] = digits[i-1] + 1
                overflow = False

            if i == len(digits) - 1 and overflow:
                if digits[i] + 1 > 9:
                    digits[i] = 0
                    digits.append(1)
                else:
                    digits[i] = digits[i] + 1      
                break 
            
            i += 1
        
        return list(reversed(digits))