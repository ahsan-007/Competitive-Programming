# https://leetcode.com/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.isInterleaveUtil(s1, s2, s3, {})

    def isInterleaveUtil(self, s1: str, s2: str, s3: str, memo) -> bool:
        if len(s3) == 0:
            return True if len(s1) == 0 and len(s2) == 0 else False

        if (s1, s2, s3) in memo:
            return memo[(s1, s2, s3)]

        if len(s1) and s1[0] == s3[0] and self.isInterleaveUtil(s1[1:], s2, s3[1:], memo):
            memo[(s1, s2, s3)] = True
            return True

        if len(s2) and s2[0] == s3[0]:
            memo[(s1, s2, s3)] = self.isInterleaveUtil(
                s1, s2[1:], s3[1:], memo)
            return memo[(s1, s2, s3)]

        memo[(s1, s2, s3)] = False
        return False


print(Solution().isInterleave(s1="aabcc"*20, s2="dbbca"*20, s3="aadbbcbcac"*20))
print(Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
print(Solution().isInterleave(s1="", s2="", s3=""))
