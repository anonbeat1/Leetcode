from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums)):
            if idx+1 < len(nums):
                if nums[idx] == nums[idx+1]:
                    nums[idx] = nums[idx]*2
                    nums[idx+1] = 0
        left = 0
        
        for rigth in range(len(nums)): ##Shifto gli 0 alla fine , considerando solamente i numeri maggiori di 0 e switchando posizione tra left e rigth 
            if nums[rigth] != 0:
                nums[rigth],nums[left] = nums[left],nums[rigth]
                left += 1
        return nums

        
x = Solution()
print(x.applyOperations([1,2,2,1,1,0]))