from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        nums_map = {}
        for index, num in enumerate(nums):
            if target - num in nums_map:
                return index, nums_map.get(target - num)
            else:
                nums_map.update({num: index})