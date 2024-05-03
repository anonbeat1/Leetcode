from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res_list = list()
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        frequency = list(sorted(frequency.items(), key=lambda x: x[1],reverse=True))
        
        for i in range(k):
            res_list.append(frequency[i][0])
        return res_list

        
x = Solution()
print(x.topKFrequent([4,1,-1,2,-1,2,3],2))  