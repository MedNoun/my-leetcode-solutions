class MinStack:

    m_stk : list
    stk : list

    def __init__(self):
        self.m_stk = []
        self.stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.m_stk) == 0 or self.m_stk[-1] >= val:
            self.m_stk.append(val)
    def pop(self) -> None:
        lts = self.stk.pop() if len(self.stk)>0 else None
        if lts != None and lts == self.m_stk[-1]:
            self.m_stk.pop()
        return lts

    def top(self) -> int:
        return self.stk[-1] if len(self.stk)>0 else None
        

    def getMin(self) -> int:
        return self.m_stk[-1] if len(self.m_stk)>0 else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()