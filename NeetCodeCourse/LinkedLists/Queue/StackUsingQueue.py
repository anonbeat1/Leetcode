from collections import deque
class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        for _ in range(len(self.stack) -1 ):
            self.push(self.stack.popleft())
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


#Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(1)
print(obj.top())