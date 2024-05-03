from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr_len = len(nums)
        set_arr = set(nums)
        if arr_len > len(set_arr):
            return True
        else:
            return False


x = Solution()
print(x.containsDuplicate([1,2,3,3,4,5]))        