# https://leetcode.com/problems/fancy-sequence/description/?envType=daily-question&envId=2026-03-15


class Fancy:

    mod = int(1e9+7)

    def __init__(self):
        self.sequence = []
        self.a = [1]
        self.b = [0]

    def mulUtil(self, x: int, y: int) -> int:
        return pow(x, y, self.mod)

    def multiplicativeInverse(self, x: int) -> int:
        return self.mulUtil(x, self.mod - 2)

    def append(self, val: int) -> None:
        self.sequence.append(val)
        self.a.append(self.a[-1])
        self.b.append(self.b[-1])

    def addAll(self, inc: int) -> None:
        self.b[-1] = (self.b[-1] + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.a[-1] = (self.a[-1] * m) % self.mod
        self.b[-1] = (self.b[-1] * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if 0 <= idx < len(self.sequence):
            ao = self.multiplicativeInverse(self.a[idx]) * self.a[-1]
            bo = self.b[-1] - self.b[idx] * ao
            return (ao * self.sequence[idx] + bo) % self.mod
        return -1


obj = Fancy()
obj.append(2)
obj.addAll(4)
obj.multAll(8)
print(obj.getIndex(0))
