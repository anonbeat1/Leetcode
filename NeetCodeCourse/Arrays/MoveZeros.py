from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None: 
        left = 0
        for rigth in range(0,len(nums)):
            if nums[rigth] != 0:
                nums[left],nums[rigth] = nums[rigth],nums[left] ##SWAPPARE POSIZIONE ARRAY
                left += 1 
        return nums


x = Solution()
print(x.moveZeroes([0,1,0,3,12]))