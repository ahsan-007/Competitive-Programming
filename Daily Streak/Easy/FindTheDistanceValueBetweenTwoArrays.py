# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/?envType=daily-question&envId=2026-11-05

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        for num in arr1:
            j = 0
            while j < len(arr2) and abs(num - arr2[j]) > d:
                j = j + 1

            if j == len(arr2):
                count += 1
        return count


print(Solution().findTheDistanceValue(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2))
print(Solution().findTheDistanceValue(
    arr1=[1, 4, 2, 3], arr2=[-4, -3, 6, 10, 20, 30], d=3))
print(Solution().findTheDistanceValue(
    arr1=[2, 1, 100, 3], arr2=[-5, -2, 10, -3, 7], d=6))
