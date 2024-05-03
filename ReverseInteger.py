class Solution:
    def reverse(self, x: int) -> int:
        maxValue = 2147483647
        minValue = -2147483647

        reversed = str(x)[::-1]
        try:            
            if "-" in reversed:
                reversed = int("{}{}".format("-",reversed.split('-')[0]))
            else:
                reversed = int(reversed)
            if reversed > maxValue or reversed < minValue:
                return 0
            else:
                return int(reversed)
        except Exception as e:
            return 0
x = Solution()
print(x.reverse(-2147483648))