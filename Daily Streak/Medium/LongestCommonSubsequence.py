# https://leetcode.com/problems/longest-common-subsequence/description/?envType=daily-question&envId=2024-01-25

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def longestCommonSubsequenceUtil(s1, s2, i, j, memo):
            if i == len(s1) or j == len(s2):
                return 0

            if (i, j) not in memo:
                if s1[i] == s2[j]:
                    memo[(i, j)] = 1 + \
                        longestCommonSubsequenceUtil(
                            s1, s2, i + 1, j + 1, memo)
                else:
                    memo[(i, j)] = max(longestCommonSubsequenceUtil(s1, s2, i + 1, j, memo),
                                       longestCommonSubsequenceUtil(s1, s2, i, j + 1, memo))

            return memo[(i, j)]

        return longestCommonSubsequenceUtil(text1, text2, 0, 0, {})


print(Solution().longestCommonSubsequence(text1="abcde", text2="ace"))
print(Solution().longestCommonSubsequence(text1="abc", text2="abc"))
print(Solution().longestCommonSubsequence(text1="abc", text2="def"))
