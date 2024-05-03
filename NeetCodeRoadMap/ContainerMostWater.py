from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        rigth = len(height)-1
        max_area = 0
        while left < rigth:
            # print("LEFT {} - RIGTH {}".format(height[left],height[rigth]))
            area = None
            if height[left] > height[rigth]:
                area = height[rigth] * (rigth - left)
                rigth -= 1
            else:
                area = height[left] * (rigth - left)
                left +=1
            if area > max_area:
                max_area = area
        return max_area

x = Solution()
print(x.maxArea([1,8,6,2,5,4,8,3,7]))
'''
First run 12 2*6
Second Run 15 3 *5
Third Run 16 4*4

'''


'''
[1,8,6,2,5,4,8,3,7]
   ^             ^
'''