# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

from collections import Counter
from pprint import pprint


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_freq = Counter(s)
        t_freq = Counter(t)
        steps = 0

        for ch in s_freq:
            count = t_freq.get(ch, 0)
            if count < s_freq[ch]:
                steps = steps + (s_freq[ch] - count)

        for ch in t_freq:
            count = s_freq.get(ch, 0)
            if count < t_freq[ch]:
                steps = steps + (t_freq[ch] - count)

        return steps


print(Solution().minSteps('leetcode', 'coats'))
print(Solution().minSteps('night', 'thing'))
