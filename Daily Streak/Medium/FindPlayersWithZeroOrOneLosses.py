# https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/?envType=daily-question&envId=2024-01-15

from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss = {}
        for match in matches:
            loss[match[1]] = loss.get(match[1], 0) + 1
            if match[0] not in loss:
                loss[match[0]] = 0

        players = list(loss.keys())
        players.sort()

        answer = [[], []]
        for player in players:
            if loss[player] == 0:
                answer[0].append(player)
            elif loss[player] == 1:
                answer[1].append(player)
        return answer


print(Solution().findWinners(matches=[[1, 3], [2, 3], [3, 6], [
      5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))

print(Solution().findWinners(matches=[[2, 3], [1, 3], [5, 4], [6, 4]]))
