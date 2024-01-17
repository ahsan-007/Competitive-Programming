# https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=daily-question&envId=2024-01-16

import random


class RandomizedSet:

    def __init__(self):
        self.element_to_index = {}
        self.index_to_element = {}
        self.no_of_elements = 0

    def insert(self, val: int) -> bool:
        if val not in self.element_to_index:
            self.index_to_element[self.no_of_elements] = val
            self.element_to_index[val] = self.no_of_elements
            self.no_of_elements = self.no_of_elements + 1
            return True

        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.element_to_index:
            ind = self.element_to_index[val]
            del self.element_to_index[val]

            if ind != self.no_of_elements - 1:
                last_element = self.index_to_element[self.no_of_elements - 1]
                self.index_to_element[ind] = last_element
                self.element_to_index[last_element] = ind

            del self.index_to_element[self.no_of_elements - 1]
            self.no_of_elements = self.no_of_elements - 1

            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.index_to_element[random.randint(0, self.no_of_elements - 1)]


obj = RandomizedSet()

obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)

print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())


print(obj.remove(2))
print(obj.remove(3))


print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
