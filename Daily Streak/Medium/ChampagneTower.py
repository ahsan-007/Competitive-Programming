# https://leetcode.com/problems/champagne-tower/description/?envType=daily-question&envId=2026-02-14

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0] * 102 for i in range(102)]
        glasses[0][0] = poured
        for i in range(query_row + 1):
            for j in range(query_glass + 1):
                q = (glasses[i][j] - 1) / 2
                if q > 0:
                    glasses[i+1][j] += q
                    glasses[i+1][j+1] += q
        return min(1, glasses[query_row][query_glass])


print(Solution().champagneTower(poured=1, query_row=1, query_glass=1))
print(Solution().champagneTower(poured=2, query_row=1, query_glass=1))
print(Solution().champagneTower(poured=6, query_row=2, query_glass=0))
print(Solution().champagneTower(poured=6, query_row=2, query_glass=1))
print(Solution().champagneTower(poured=6, query_row=2, query_glass=2))
print(Solution().champagneTower(poured=7, query_row=3, query_glass=0))
print(Solution().champagneTower(poured=8, query_row=3, query_glass=0))
print(Solution().champagneTower(poured=7, query_row=3, query_glass=1))
print(Solution().champagneTower(poured=7, query_row=3, query_glass=2))
print(Solution().champagneTower(poured=7, query_row=3, query_glass=3))
print(Solution().champagneTower(poured=4, query_row=1, query_glass=1))
print(Solution().champagneTower(poured=100000009, query_row=33, query_glass=1))
