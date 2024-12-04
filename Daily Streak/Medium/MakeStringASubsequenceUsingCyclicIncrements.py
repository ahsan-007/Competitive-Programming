# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/description /?envType=daily-question&envId=2024-12-04


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        def incrementChar(ch):
            return chr(ord('a') + (((ord(ch) + 1) - ord('a')) % 26))

        str1Index = 0
        str2Index = 0
        while str1Index < len(str1) and str2Index < len(str2):
            if str1[str1Index] == str2[str2Index] or incrementChar(str1[str1Index]) == str2[str2Index]:
                str2Index = str2Index + 1

            str1Index = str1Index + 1

        return str2Index == len(str2)


print(Solution().canMakeSubsequence(str1="abc", str2="ad"))
print(Solution().canMakeSubsequence(str1="zc", str2="ad"))
print(Solution().canMakeSubsequence(str1="ab", str2="d"))
