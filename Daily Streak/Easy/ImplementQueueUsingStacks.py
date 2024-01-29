# https://leetcode.com/problems/implement-queue-using-stacks/description/?envType=daily-question&envId=2024-01-29

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            self.prepareStack2()

        return self.stack2.pop() if self.stack2 else None

    def peek(self) -> int:
        if not self.stack2:
            self.prepareStack2()

        return self.stack2[-1] if self.stack2 else None

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def prepareStack2(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
