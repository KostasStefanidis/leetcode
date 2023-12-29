from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or not nums2:
            return nums1 or nums2
        
        i = 0
        while m < len(nums1):
            nums1[m] = nums2[i]
            i += 1
            m += 1
           
        nums1.sort()