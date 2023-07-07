# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        return max(self.maximumConsecutiveCount(answerKey, k, 'T'), self.maximumConsecutiveCount(answerKey, k, 'F'))

    def maximumConsecutiveCount(Self, answerKey: str, k, ans):
        i = j = 0
        flipped = []
        maximumCount = 0
        while j < len(answerKey):
            if answerKey[j] == ans:
                j = j + 1
            else:
                if k > 0:
                    flipped.append(j)
                    j = j + 1
                    k = k - 1
                else:
                    flipped_key = flipped.pop(0)
                    i = flipped_key + 1
                    k = k + 1
            maximumCount = max(maximumCount, j-i)
        return maximumCount


print(Solution().maxConsecutiveAnswers(answerKey="TTFF", k=2))
print(Solution().maxConsecutiveAnswers(answerKey="TFFT", k=1))
print(Solution().maxConsecutiveAnswers(answerKey="TTFTTFTT", k=1))
