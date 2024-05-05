# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        def search(low,high):
            while low <= high:
                m = (low + high) // 2
                if not isBadVersion(m):
                    low = m+1
                else:
                    high = m-1
            return low
        return search(0,n)
                
'''
[0,1,2,3,4] -> 2 -> isBad? True -> high = m-1
[0,1] -> 0 -> isBad? False -> low = m+1 
[1,1] -> 1 -> isBad? True -> Return True
'''