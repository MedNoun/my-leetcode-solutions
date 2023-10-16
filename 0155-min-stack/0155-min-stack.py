class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not len(self.min_stack):
            self.min_stack.append(val)
        else:
            last_min = self.min_stack.pop()
            new_min = min(last_min, val)
            self.min_stack.append(last_min)
            self.min_stack.append(new_min)
    def pop(self) -> None:
        self.min_stack.pop()
        return self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()