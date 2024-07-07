# https://leetcode.com/problems/water-bottles/description /?envType=daily-question&envId=2024-07-07

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        maxDrankBottles = 0
        emptyBottles = 0
        while numBottles > 0:
            maxDrankBottles += numBottles
            emptyBottles = emptyBottles + numBottles

            numBottles = emptyBottles // numExchange
            emptyBottles = emptyBottles % numExchange

        return maxDrankBottles


print(Solution().numWaterBottles(9, 3))
print(Solution().numWaterBottles(9, 2))
print(Solution().numWaterBottles(15, 4))
