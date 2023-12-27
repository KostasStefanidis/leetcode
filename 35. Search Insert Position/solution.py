# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # [0,1,2,3,5,6] target=4
        if target in nums:
            return nums.index(target)
        else:
            for elem in nums:
                if target < elem:
                    return nums.index(elem)
        
        return len(nums)