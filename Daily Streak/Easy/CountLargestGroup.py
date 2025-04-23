# https://leetcode.com/problems/count-largest-group/description/?envType=daily-question&envId=2025-04-23

class Solution:
    def countLargestGroup(self, n: int) -> int:
        def getDigitSum(num):
            digitSum = 0
            while num:
                digitSum = digitSum + num % 10
                num = num // 10
            return digitSum

        groupCount = {}

        for i in range(1, n + 1):
            digitSum = getDigitSum(i)
            groupCount[digitSum] = groupCount.get(digitSum, 0) + 1

        max_size = max(groupCount.values())
        return sum(1 if groupCount[key] == max_size else 0 for key in groupCount)


print(Solution().countLargestGroup(n=13))
