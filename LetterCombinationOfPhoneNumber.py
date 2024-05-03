from typing import List
import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = list()
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if len(digits) == 0:
            return []
        return itertools.
x = Solution()
print(x.letterCombinations("234"))

        