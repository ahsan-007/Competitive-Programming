# https://leetcode.com/problems/flatten-nested-list-iterator/description/?envType=daily-question&envId=2023-10-20


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> ['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList: ['NestedInteger']):
        def flatten(nestedList):
            flaten_list = []
            for ele in nestedList:
                if ele.isInteger():
                    flaten_list.append(ele.getInteger())
                else:
                    flaten_list.extend(flatten(ele.getList()))
            return flaten_list

        self.flat_list = flatten(nestedList)
        self.i = 0

    def next(self) -> int:
        self.i = self.i + 1
        return self.flat_list[self.i - 1]

    def hasNext(self) -> bool:
        return self.i < len(self.flat_list)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
