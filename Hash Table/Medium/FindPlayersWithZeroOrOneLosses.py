# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = {}
        for match in matches:
            if match[0] not in players:
                players[match[0]] = 0

            if match[1] not in players:
                players[match[1]] = 0
            players[match[1]] += 1

        answer = [[], []]
        for player in players.keys:
            if players[player] == 0:
                answer[0].append(player)
            elif players[player] == 1:
                answer[1].append(player)
        answer[0].sort()
        answer[1].sort()
        return answer


print(Solution().findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [
      5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))

print(Solution().findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]))
