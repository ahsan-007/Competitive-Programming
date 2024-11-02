# https://leetcode.com/problems/circular-sentence/description /?envType=daily-question&envId=2024-11-02

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        i = 0
        while i < len(sentence):
            if sentence[i] == ' ':
                if sentence[i-1] != sentence[i+1]:
                    return False
            i = i + 1
        return True


print(Solution().isCircularSentence(
    sentence="leetcode exercises sound delightful"))
print(Solution().isCircularSentence(sentence="eetcode"))
print(Solution().isCircularSentence(sentence="Leetcode is cool"))
print(Solution().isCircularSentence(sentence="Leetcode"))
