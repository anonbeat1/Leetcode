from typing import List

class Solution:
    def twoSum(self,nums,target) -> List[int]:
        print(nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
x = Solution()
print(x.twoSum([2,7,11,15],9))