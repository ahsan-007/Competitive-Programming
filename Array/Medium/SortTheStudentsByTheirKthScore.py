# https://leetcode.com/problems/sort-the-students-by-their-kth-score/

from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(score)):
            max = i
            for j in range(i+1, len(score)):
                if score[j][k] > score[max][k]:
                    max = j
            score[i], score[max] = score[max], score[i]
        return score


print(Solution().sortTheStudents(score=[[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]], k=2
                                 ))
print(Solution().sortTheStudents(score=[[3, 4], [5, 6]], k=0))
