# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description /?envType=daily-question&envId=2024-10-04

from typing import List
from collections import Counter


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total_skill = sum(skill)
        target = total_skill // (len(skill) // 2)
        if (total_skill / (len(skill) // 2)) - target > 0:
            return -1
        freq = Counter(skill)
        chemistry = 0
        current_sum = 0
        for ele in skill:
            if (ele * 2 == target and freq.get(ele, 0) > 1) or (ele * 2 != target and freq.get(ele, 0) > 0 and freq.get(target - ele, 0) > 0):
                chemistry = chemistry + ele * (target - ele)
                freq[ele] = freq[ele] - 1
                freq[target - ele] = freq[target - ele] - 1
                current_sum = current_sum + target
        return chemistry if total_skill == current_sum else -1


print(Solution().dividePlayers(skill=[3, 2, 5, 1, 3, 4]))
print(Solution().dividePlayers(skill=[3, 4]))
print(Solution().dividePlayers(skill=[1, 1, 2, 3]))
