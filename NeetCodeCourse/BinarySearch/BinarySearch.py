from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, rigth = 0, len(nums) - 1

        while left <= rigth:
            m = (left + rigth) // 2
            if target > nums[m]:
                left = m+1
            elif target < nums[m]:
                rigth = m-1
            else:
                return m
        return -1


x = Solution()
print(x.search([-1,0,3,5,9,12],9))