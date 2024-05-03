from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        solutions = list()
        for startValue in range(len(nums)):
            left = startValue +1 
            right = len(nums) -1 
            while left < right:
                operation = nums[startValue] + nums[left] + nums[right]
                if operation > target:
                    right -= 1
                elif operation < target:
                    left += 1
                else:
                    solutions.append(operation)
                    break
                solutions.append(operation)
        return min(solutions, key=lambda x: abs(x - target))

x = Solution()
print(x.threeSumClosest([0,1,2],3))