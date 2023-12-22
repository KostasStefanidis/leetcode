from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        while i < len(nums) - 1:
            tmp = nums.pop(i)
            
            while tmp in nums:
                nums.remove(tmp)
            
            tmp = nums.insert(i, tmp)
            
            i = i + 1

        return len(nums)