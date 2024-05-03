from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = set()
        for i in range(len(nums)):
            for x in range(i+1,len(nums)):
                for z in range(i+2,len(nums)):
                     if nums[i] + nums[x] + nums[z] == 0 and i is not x and x is not z:
                        sorted_nums = [nums[i],nums[x],nums[z]]
                        sorted_nums.sort()
                        solutions.add(tuple(sorted_nums))
        return list(solutions)

class SolutionTwo:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = set()
        nums.sort()

        for initialValue in range(len(nums)):
            left = initialValue + 1
            right = len(nums) -1
            while left < right:
                print("initialvalue {},left {},right {}".format(initialValue,left,right))
                operation = nums[initialValue] + nums[left] + nums[right]
                print("operation {}".format(operation))
                if operation > 0:
                    right -= 1          
                elif operation < 0:
                    left += 1
                else:
                    solutions.add(tuple([nums[initialValue],nums[left],nums[right]]))
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                continue
        return list(solutions)
        
    


x = SolutionTwo()
print(x.threeSum([-1,0,1,2,-1,-4]))