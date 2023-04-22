# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

class Solution:
    def minInsertions(self, s: str) -> int:
        return self.minInsertionsUtil(s, {})

    def minInsertionsUtil(self, s, memo):
        if len(s) <= 1:
            return 0
        if s not in memo:
            if s[0] == s[-1]:
                operations = self.minInsertionsUtil(s[1:-1], memo)
            else:
                operations = min(
                    self.minInsertionsUtil(s[1:], memo),
                    self.minInsertionsUtil(s[:-1], memo)) + 1
            memo[s] = operations
        return memo[s]


print(Solution().minInsertions('zzazz'))
print(Solution().minInsertions('mbadm'))
print(Solution().minInsertions('leetcode'))
print(Solution().minInsertions('zjveiiwvc'))
print(Solution().minInsertions(''.join(['a', 'z', 'v', 'w', 'i'] * 20)))
