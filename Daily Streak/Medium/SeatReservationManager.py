# https://leetcode.com/problems/seat-reservation-manager/description/?envType=daily-question&envId=2023-11-06

class SeatManager:
    class Heap:
        def __init__(self):
            self.elements = []

        def buildHeap(self, elenments):
            self.elements = [ele for ele in elenments]
            i = len(elenments) // 2 - 1
            for i in range(len(elenments) // 2, -1, -1):
                self.heapify(i)

        def getMin(self):
            if len(self.elements) == 0:
                return
            minEle = self.elements[0]
            if len(self.elements) != 1:
                self.elements[0] = self.elements.pop(-1)
                self.heapify(0)
            else:
                self.elements = []
            return minEle

        def addEle(self, ele):
            self.elements.append(ele)
            self.heapifyBottomUp(len(self.elements) - 1)

        def heapify(self, i):
            if 2 * i >= len(self.elements):
                return

            if 2 * i + 1 < len(self.elements):
                if self.elements[2 * i] < self.elements[i] and self.elements[2*i] < self.elements[2*i+1]:
                    self.elements[i], self.elements[2 *
                                                    i] = self.elements[2*i], self.elements[i]
                    self.heapify(2 * i)
                elif self.elements[2 * i + 1] < self.elements[i] and self.elements[2 * i + 1] < self.elements[2*i]:
                    self.elements[i], self.elements[2 *
                                                    i + 1] = self.elements[2*i + 1], self.elements[i]
                    self.heapify(2 * i + 1)

            else:
                if self.elements[2 * i] < self.elements[i]:
                    self.elements[i], self.elements[2 *
                                                    i] = self.elements[2*i], self.elements[i]
                    self.heapify(2 * i)

        def heapifyBottomUp(self, i):
            if i <= 0:
                return

            if self.elements[i] < self.elements[i // 2]:
                self.elements[i], self.elements[i //
                                                2] = self.elements[i//2], self.elements[i]
                self.heapifyBottomUp(i // 2)

    def __init__(self, n: int):
        self.heap = SeatManager.Heap()
        self.heap.buildHeap([i for i in range(1, n + 1)])

    def reserve(self) -> int:
        return self.heap.getMin()

    def unreserve(self, seatNumber: int) -> None:
        self.heap.addEle(seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
