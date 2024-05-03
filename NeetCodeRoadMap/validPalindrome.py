import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        original_cleaned_str = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        print(original_cleaned_str)
        if(original_cleaned_str[::-1] == original_cleaned_str):
            return True
        else:
            return False
        
x = Solution()
print(x.isPalindrome("ab_a"))