# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/?envType=daily-question&envId=2026-02-07


class Solution:
    def minimumDeletions(self, s: str) -> int:
        aAfter = s.count('a')
        bBefore = 0
        minDeletions = float("+inf")
        for i in range(len(s)):
            if s[i] == 'a':
                aAfter -= 1

            minDeletions = min(minDeletions, aAfter + bBefore)

            if s[i] == 'b':
                bBefore += 1
        return minDeletions


print(Solution().minimumDeletions(s="aababbab"))
print(Solution().minimumDeletions(s="bbaaaaabb"))
print(Solution().minimumDeletions(s="aaaa"))
print(Solution().minimumDeletions(s="bbbb"))
print(Solution().minimumDeletions(s="bbbba"))
print(Solution().minimumDeletions(
    s="ababaaaabbbbbaaababbbbbbaaabbaababbabbbbaabbbbaabbabbabaabbbababaa"))
print(Solution().minimumDeletions(
    s="abbbaabababababbbbbbaababbabbabbbabbaaabbbbbabbaabbbabbaabbabbbbabbabbaaaabbaabbbabbbaaabaabbaabaaababaaabbabaababbbaababbbaabaabaabbbbabaaaaabbabaaababbbbbaabbabbaabaabbababbbaaaababababababaaabaaaabbbbbbabbaaaabbabbaababbabbaaaaaaaaaababbbbaabaababaaabababbbabbbaabbbaaaaabaababbaabaaabaabbbaababbbbbababaabbbbabaabaabbaabbabaabbaaaaaaaabbbbababaaabaaaaabaaaabbaabaabbbbbbabaaaaaaababaabbbabababbabbbbbbabaabbbabbbababbbbbaaaaabbaaababbababbabbbbabababbabaaabababaabbaaaababbbabababbbaabaababbbaabababbabababbbabababbbbabaaabbbbbbabbbaaaaaabbabbaaaabbabbaaababaabaaaaabaababaaabaaaabbaabbababbbabbabbbabbbababbabbbbabaabaaaaababaaabababbaabbbaaaababbaababababaaaaaabbaaaabbbaaabbabaaaaabbabbbbbaabbabaabbbbbababaaaabbbabbababababbaabaabaababbbaaaababbbbabbbabbbabbbaabbabbaaabbabaaaaaaaaaaabbbaabbbaabbbbaaabaaabbaababaaaababaaaabbbbbaaabababaababaaabaaabbaababaababbaaaaaabaaaababbabbaaabbbabaababbbaabaaaabbaabababbbbbababaaabbaaaaabbbbbabbaabaaaabbbababbbbaababbbabaabaaabaaabaaabababaaaabaaaaaabbaabaaaaaababbbbaaaabbbaabbaaababbbaaaabbaabbaabbabaaababbbaaaabaabaababaaabaababbbababbbbaabbababbaabbbbbbaabaaaaaababbbaaaaaaabaaba"))
