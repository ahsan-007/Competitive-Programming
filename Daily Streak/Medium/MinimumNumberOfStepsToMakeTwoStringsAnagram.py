# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/?envType=daily-question&envId=2024-01-13

from collections import Counter


class Solution:
    # Time: O(N + M)
    # Space: O(1) (s and t contain only lowercase english letters)
    def minSteps(self, s: str, t: str) -> int:
        t_freq = Counter(t)
        s_freq = Counter(s)

        count = 0
        for ch in t_freq:
            count = count + abs(t_freq[ch] - s_freq.get(ch, 0))

        count = count + sum(s_freq[ch] for ch in s_freq if ch not in t_freq)

        return count // 2

    # Time: O(N)
    # Space: O(1) (s and t contains only lowercase charcaters)
    def minStepsV2(self, s: str, t: str) -> int:
        t_freq = Counter(t)
        s_freq = Counter(s)
        return sum(t_freq[ch] - s_freq[ch] for ch in t_freq if t_freq[ch] > s_freq.get(ch, 0))


print(Solution().minSteps("bab", "aba"))
print(Solution().minSteps(s="leetcode", t="practice"))

print(Solution().minStepsV2("bab", "aba"))
print(Solution().minStepsV2(s="leetcode", t="practice"))
