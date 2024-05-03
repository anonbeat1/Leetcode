from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:   
        numSet = set(nums)     
        longest = 0
        for x in numSet:
            if x-1 not in numSet:
                counter = 0
                while x +counter  in numSet:
                    counter +=1 
                print(longest)
                longest = max(counter,longest)                   
        return longest

x = Solution()
print(x.longestConsecutive([100,4,200,1,3,2]))