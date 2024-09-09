class MinStack:

    def __init__(self):
        self.s = []
        self.t = []
        

    def push(self, val: int) -> None:
        self.s.append(val)
        min = val if len(self.t) < 1 or val < self.t[len(self.t) - 1] else self.t[len(self.t) - 1]
        self.t.append(min)
        

    def pop(self) -> None:
        self.t.pop()
        self.s.pop()

    def top(self) -> int:
        return self.s[len(self.s) - 1]

    def getMin(self) -> int:
        return self.t[len(self.t) - 1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Test cases
s = MinStack()
s.push(-2)
s.push(0)
s.push(-3)
print(s.getMin()) # Expected -3