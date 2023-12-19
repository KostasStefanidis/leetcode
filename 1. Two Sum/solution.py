from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # start_idx = 0
        # end_idx = nums.length - 1
        for idx, num in enumerate(nums):
            if target - num in nums and idx != nums.index(target - num):
                return [idx, nums.index(target - num)]