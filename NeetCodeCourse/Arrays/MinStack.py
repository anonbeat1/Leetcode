class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) > 0:
            if val <= self.getMin():
                self.minStack.append(val)
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.top() == self.getMin():
            self.minStack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.push(8)
obj.push(9)
obj.pop()
print(obj.top())
print(obj.getMin())