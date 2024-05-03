class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_list = ''.join(sorted(s))
            t_list = ''.join(sorted(t))
            print(s_list,t_list)
            if s_list == t_list:
                return True
        return False        

x = Solution()
print(x.isAnagram("anagram","nagaram"))



#buuuuuut Smarter Solution 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)