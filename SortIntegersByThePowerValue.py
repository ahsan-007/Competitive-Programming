# https://leetcode.com/problems/sort-integers-by-the-power-value/

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {1: 0}
        powers = []
        numbers = list(range(lo, hi+1))
        for i in range(lo, hi+1):
            powers.append(self.calculatePower(i, memo))

        for i in range(0, k):
            min_ind = i
            for j in range(i+1, len(powers)):
                if powers[j] < powers[min_ind] or (powers[j] == powers[min_ind] and numbers[j] < numbers[min_ind]):
                    min_ind = j

            powers[i], powers[min_ind] = powers[min_ind], powers[i]
            numbers[i], numbers[min_ind] = numbers[min_ind], numbers[i]

        return numbers[k-1]

    def calculatePower(self, num, memo={1: 0}):
        if num in memo:
            return memo[num]
        if num % 2 == 0:
            memo[num] = 1 + self.calculatePower(num // 2)
        else:
            memo[num] = 1 + self.calculatePower(num * 3 + 1)
        return memo[num]


print(Solution().getKth(10, 20, 5))
