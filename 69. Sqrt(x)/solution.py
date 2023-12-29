class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left = 2
        right = x // 2
        
        while left <= right:
            pivot = left + (right - left) // 2
            
            if pivot ** 2 < x:
                left = pivot + 1
            elif pivot ** 2 > x: 
                right = pivot - 1
            else:
                return pivot
        
        return right