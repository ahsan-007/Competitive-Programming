class MinStack:
    class StackEle:
        def __init__(self, val, minimum, next=None) -> None:
            self.val = val
            self.next = next
            self.minimum = minimum

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        self.head = MinStack.StackEle(
            val, min(val, self.head.minimum if self.head else float("+inf")), self.head)

    def pop(self) -> None:
        val = self.head.val
        self.head = self.head.next
        return val

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
