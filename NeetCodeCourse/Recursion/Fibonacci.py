class Solution:
    def fib(self, n: int) -> int:
        
        def fibonacci(n):
            if n == 0:
                return 0
            if n == 1 or n ==2:
                return 1
            return fibonacci(n-1) + fibonacci(n-2)
        return fibonacci(n)
    
x = Solution()
print(x.fib(3))