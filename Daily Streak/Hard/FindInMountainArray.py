# https://leetcode.com/problems/find-in-mountain-array/description/?envType=daily-question&envId=2023-10-12


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, arr) -> None:
        self.arr = arr
        self.get_calls = 0

    def get(self, index: int) -> int:
        self.get_calls += 1
        if self.get_calls > 100:
            raise 'To Many get() Calls'
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        mountain_top = self.find_mountain_top(
            mountain_arr, 0, mountain_arr.length() - 1)

        ind = self.binary_search(target, mountain_arr, 0, mountain_top)
        return ind if ind != -1 else self.reversed_binary_search(target, mountain_arr, mountain_top + 1, mountain_arr.length() - 1)

    def find_mountain_top(self, mountain_arr, lb, ub):
        if lb > ub:
            return -1

        if lb == ub:
            return lb

        mid = lb + (ub - lb) // 2
        ele = mountain_arr.get(mid)
        if mid != 0:
            left = mountain_arr.get(mid - 1)
        if mid != mountain_arr.length() - 1:
            right = mountain_arr.get(mid + 1)

        if mid != 0 and mid != mountain_arr.length() - 1 and ele > left and ele > right:
            return mid

        elif mid != mountain_arr.length() - 1 and (mid == 0 or left < ele < right):
            return self.find_mountain_top(mountain_arr, mid + 1, ub)

        else:
            return self.find_mountain_top(mountain_arr, lb, mid - 1)

    def binary_search(self, target, mountain_arr, lb, ub):
        if lb > ub:
            return -1

        mid = lb + (ub - lb) // 2
        ele = mountain_arr.get(mid)
        if ele == target:
            return mid
        elif target > ele:
            return self.binary_search(target, mountain_arr, mid + 1, ub)
        else:
            return self.binary_search(target, mountain_arr, lb, mid - 1)

    def reversed_binary_search(self, target, mountain_arr, lb, ub):
        if lb > ub:
            return -1

        mid = lb + (ub - lb) // 2
        ele = mountain_arr.get(mid)
        if ele == target:
            return mid
        elif target > ele:
            return self.reversed_binary_search(target, mountain_arr, lb, mid - 1)
        else:
            return self.reversed_binary_search(target, mountain_arr, mid + 1, ub)


print(Solution().findInMountainArray(
    target=3, mountain_arr=MountainArray([1, 2, 3, 4, 5, 3, 1])))

print(Solution().findInMountainArray(
    target=2, mountain_arr=MountainArray([1, 5, 2])))

print(Solution().findInMountainArray(
    target=3, mountain_arr=MountainArray([3, 5, 3, 2, 0])))

print(Solution().findInMountainArray(
    target=101, mountain_arr=MountainArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82])))
