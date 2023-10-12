# https://leetcode.com/problems/number-of-flowers-in-full-bloom/description/?envType=daily-question&envId=2023-10-11

from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starting_times = [flower[0] for flower in flowers]
        ending_times = [flower[1] for flower in flowers]

        starting_times.sort()
        ending_times.sort()

        blooming = []

        for p in people:
            started_blooming = self.get_flowers_started_blooming(
                starting_times, p, 0, len(starting_times)-1)

            ended_blooming = self.get_flowers_ended_blooming(
                ending_times, p, 0, len(ending_times) - 1)

            blooming.append(started_blooming - ended_blooming)

        return blooming

    def get_flowers_started_blooming(self, arr, ele, lb, ub):
        if lb > ub:
            return lb

        mid = lb + (ub - lb) // 2
        if arr[mid] == ele and (mid == ub or arr[mid+1] != ele):
            return mid + 1
        elif arr[mid] > ele:
            if mid != lb and arr[mid - 1] < ele:
                return mid
            return self.get_flowers_started_blooming(arr, ele, lb, mid-1)
        else:
            if mid != ub and arr[mid + 1] > ele:
                return mid + 1
            return self.get_flowers_started_blooming(arr, ele, mid + 1, ub)

    def get_flowers_ended_blooming(self, arr, ele, lb, ub):
        if lb > ub:
            return lb

        mid = lb + (ub - lb) // 2
        if arr[mid] == ele:
            return self.get_flowers_ended_blooming(arr, ele, lb, mid-1)
        elif arr[mid] > ele:
            if mid != lb and arr[mid - 1] < ele:
                return mid
            return self.get_flowers_ended_blooming(arr, ele, lb, mid-1)
        else:
            if mid != ub and arr[mid + 1] > ele:
                return mid + 1
            return self.get_flowers_ended_blooming(arr, ele, mid + 1, ub)


print(Solution().fullBloomFlowers(
    flowers=[[1, 6], [3, 7], [9, 12], [4, 13]], people=[2, 3, 7, 11]))

print(Solution().fullBloomFlowers(flowers=[[1, 10], [3, 3]], people=[3, 3, 2]))

print(Solution().fullBloomFlowers(flowers=[[50, 50], [19, 27], [40, 46], [
      42, 48], [22, 46], [41, 50], [11, 36], [14, 29]], people=[17, 35, 38]))
