# https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        if len(self.queue2) == 0:
            self.queue1.append(x)
        else:
            self.queue2.append(x)

    def pop(self) -> int:
        if len(self.queue2) == 0:
            if len(self.queue1) == 0:
                return None

            while len(self.queue1) != 1:
                self.queue2.append(self.queue1.pop(0))

            return self.queue1.pop()
        else:
            if len(self.queue2) == 0:
                return None

            while len(self.queue2) != 1:
                self.queue1.append(self.queue2.pop(0))

            return self.queue2.pop()

    def top(self) -> int:
        if len(self.queue2) != 0:
            return self.queue2[-1]

        if len(self.queue1) != 0:
            return self.queue1[-1]

        return None

    def empty(self) -> bool:
        return len(self.queue1) == 0 and len(self.queue2) == 0


stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.top())
print(stack.pop())
stack.push(5)
print(stack.top())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.empty())
print(stack.pop())
print(stack.empty())
