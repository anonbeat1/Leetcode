from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) -1
        row = None
        while top <= bottom:

            m = (top + bottom) //2
            if target > matrix[m][-1]:
                top = m +1
            elif target < matrix[m][0]:
                bottom = m -1
            else:
                row = m
                break

        if row is not None:
            left, rigth = 0, len(matrix[row]) -1
            while left <= rigth:
                mr = (left + rigth) // 2
                if target > matrix[row][mr]:
                    left = mr +1
                elif target < matrix[row][mr]:
                    rigth = mr - 1
                else:
                    return True
        return False

x = Solution()
print(x.searchMatrix([[1]],0))

