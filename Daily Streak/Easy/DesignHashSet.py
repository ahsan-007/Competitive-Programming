# https://leetcode.com/problems/design-hashset/description/

class MyHashSet:

    def __init__(self):
        self.map = [False for i in range(1000000)]

    def add(self, key: int) -> None:
        self.map[key] = True

    def remove(self, key: int) -> None:
        self.map[key] = False

    def contains(self, key: int) -> bool:
        return self.map[key]
