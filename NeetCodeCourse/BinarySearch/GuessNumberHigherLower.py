# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        def search(low,high):
            while low <= high:
                m = (low+high) // 2
                solution = self.guess(m)
                if solution == -1:
                    high = m-1
                elif solution == 1:
                    low = m+1
                else:
                    return m
        return search(0,n)