from typing import List
'''
Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        left, rigth = 0,len(nums)-1
        while left <= rigth:
            m = (left+rigth) //2
            if nums[m] > nums[m:][-1]:
                left = m+1
            else:
                rigth = m-1
        return nums[left]

x = Solution()        
print(x.findMin([3,4,5,1,2]))
'''
left = 0
rigth = 4
[3,4,5,1,2] -> 2
   ^
left = 2
rigth = 4
[3,4,5,1,2] -> 3
     ^

left = 0
rigth = 4
[11,13,15,17] -> 2 
    ^
left =  0
rigth = 3
1
'''