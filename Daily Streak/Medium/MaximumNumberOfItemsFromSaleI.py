# https://leetcode.com/problems/maximum-number-of-items-from-sale-i/description/?envType=daily-question&envId=2026-11-27

from typing import List

from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        totalItems = []
        minPrice = float("+inf")
        for i in range(len(items)):
            minPrice = min(items[i][1], minPrice)
            count = 0
            for j in range(len(items)):
                if items[j][0] % items[i][0] == 0:
                    count += 1
            totalItems.append(tuple(items[i]) + (count,))

        dp = [b // minPrice for b in range(budget + 1)]

        for _, price, count in totalItems:
            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + count)

        return dp[budget]
        


print(Solution().maximumSaleItems(items = [[6,2],[2,6],[3,4]], budget = 9))
print(Solution().maximumSaleItems(items = [[2,4],[3,2],[4,1],[6,4],[12,4]], budget = 8))
print(Solution().maximumSaleItems(items = [[28,1],[56,4],[56,42]], budget = 45))
print(Solution().maximumSaleItems(items = [[979,37],[493,42],[265,16],[1065,8],[1410,13],[513,54],[1354,1],[1,36],[304,41],[106,53],[1158,33],[920,48],[1236,41],[1055,65],[1498,61],[716,59],[515,47],[1494,51],[1228,22],[365,19],[818,64],[92,45],[86,67],[403,18],[1198,34],[1358,18],[122,57],[1390,40],[291,55],[631,65],[921,5],[168,9],[274,63],[309,59],[475,59],[806,1],[400,64],[1312,14],[1428,40],[360,7],[1354,51],[291,21],[888,57],[651,28],[933,26],[1124,64],[481,16],[2,31],[706,50],[1295,38],[509,28],[30,54],[736,52],[604,55],[630,8],[1422,58],[1321,60],[1261,50],[1256,38],[960,20],[653,27],[915,47],[62,4],[1087,59],[1410,67],[177,45],[565,13],[1170,3],[1272,63],[1353,56],[444,8],[385,9],[497,49],[176,1],[217,56],[1039,60],[899,16],[645,2],[574,27],[609,11]],
                                   budget = 67))
print(Solution().maximumSaleItems(items = [[44,22],[44,32],[44,38],[44,17],[44,24]], budget = 38))
print(Solution().maximumSaleItems(items = [[1,5],[14,23],[6,23],[30,8],[85,26],[57,26],[90,5],[60,29],[60,11]], budget = 31))
