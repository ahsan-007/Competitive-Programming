# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/?envType=daily-question&envId=2026-11-01

class Solution:
    # TLE
    def minMoves(self, nums: list[int]) -> int:
        found = len(set(nums)) == 1
        moves = 0
        while not found:
            min_ele = min(nums)
            max_ele = max(nums)
            ind = nums.index(max_ele)

            diff = max_ele - min_ele
            moves += diff
            count = 0

            for i in range(len(nums)):
                if i != ind:
                    nums[i] += diff

                if nums[i] == max_ele:
                    count += 1

            found = len(nums) == count
        return moves

    def minMovesV2(self, nums: list[int]) -> int:
        return sum(nums) - (len(nums) * min(nums))


print(Solution().minMoves(nums=[1, 2, 3]))
print(Solution().minMoves(nums=[1, 1, 1]))
