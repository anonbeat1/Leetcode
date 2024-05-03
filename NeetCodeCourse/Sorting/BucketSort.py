from typing import List
class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        counts = [0,0,0]

    # Count the quantity of each val in arr
        for n in arr:
            counts[n] += 1
        
        # Fill each bucket in the original array
        i = 0
        for n in range(len(counts)):
            for _ in range(counts[n]):
                arr[i] = n
                i += 1
        return arr

x = Solution()
print(x.sortArray([2,0,1]))