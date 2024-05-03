from typing import List
from collections import Counter,defaultdict

class Solution:

    ## Slow as f
    def groupAnagramsSlowAsF(self, strs: List[str]) -> List[List[str]]:
        groups = list()
        for index,word in enumerate(strs):
            print(word)
            anagrams = list()
            anagrams.append(word)
            right = len(strs)-1
            while right > index:
                if Counter(word) == Counter(strs[right]):
                    anagrams.append(strs[right])
                    strs.pop(right)
                right -= 1
            groups.append(anagrams)             
        return groups
    
    def groupAnagramsNeetCode(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            count = [0] *26
            for char in string:
                count[ord(char) -ord('a')] += 1
            groups[tuple(count)].append(string)
        return groups.values()
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            groups[''.join(sorted(string))].append(string)
        return groups
    
x = Solution()
print(x.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  