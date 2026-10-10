# https://leetcode.com/problems/minimum-sum-of-squared-difference/description/?envType=daily-question&envId=2026-10-10

import heapq


class MaxHeap:
    def __init__(self, elements=None):
        if elements:
            self.heap = [-ele for ele in elements]
            if elements:
                heapq.heapify(self.heap)
        else:
            self.heap = []

    def push(self, ele):
        heapq.heappush(self.heap, -ele)

    def pop(self):
        return -heapq.heappop(self.heap)

    def peek(self):
        if self.heap:
            return -self.heap[0]
        return None

    def get_elements(self):
        return [-ele for ele in self.heap]

    def is_empty(self):
        return self.heap is None or len(self.heap) == 0


class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(nums1[i] - nums2[i])
                for i in range(len(nums1))]

        k3 = k1 + k2
        if k3 >= sum(ele**2 for ele in diff):
            return 0

        diff_map = {}
        for d in diff:
            diff_map[d] = diff_map.get(d, 0) + 1

        max_heap = MaxHeap(list(diff_map.keys()))

        while k3 and not max_heap.is_empty():
            ele = max_heap.pop()
            if k3 >= diff_map[ele]:
                k3 = k3 - diff_map[ele]
                if ele != 0:
                    if ele - 1 not in diff_map:
                        max_heap.push(ele - 1)
                    diff_map[ele -
                             1] = diff_map.get(ele-1, 0) + diff_map[ele]
                del diff_map[ele]
            else:
                if ele != 0:
                    diff_map[ele - 1] = diff_map.get(ele-1, 0) + k3
                    diff_map[ele] = diff_map[ele] - k3
                k3 = 0
        return sum((key ** 2) * diff_map[key] for key in diff_map)


print(Solution().minSumSquareDiff(
    nums1=[1, 2, 3, 4], nums2=[2, 10, 20, 19], k1=0, k2=0))
print(Solution().minSumSquareDiff(
    nums1=[1, 4, 10, 12], nums2=[5, 8, 6, 9], k1=1, k2=1))
print(Solution().minSumSquareDiff(
    nums1=[10, 10, 10, 11, 5], nums2=[1, 0, 6, 6, 1], k1=11, k2=27))
print(Solution().minSumSquareDiff(
    nums1=[18, 4, 8, 19, 13, 8], nums2=[18, 11, 8, 2, 13, 15], k1=16, k2=8))
