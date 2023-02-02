# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        first_row = [i for i in range(0, len(word1)+1)]
        memo = [first_row]
        for j in range(1, len(word2)+1):
            memo.append([j])

        for i in range(1, len(word2)+1):
            for j in range(1, len(word1)+1):
                memo[i].append(min(memo[i][j-1] + 1,
                                   memo[i-1][j] + 1,
                                   memo[i-1][j-1] + (0 if word1[j-1] == word2[i-1] else 1)))
        return memo[len(word2)][len(word1)]


print(Solution().minDistance("zoologicoarchaeologist", "zoogeologist"))
