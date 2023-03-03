# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_frequency = Solution.find_frequency(s)
        t_frequency = Solution.find_frequency(t)
        steps = 0
        for ch in s_frequency:
            if ch in t_frequency:
                if t_frequency[ch] < s_frequency[ch]:
                    steps = steps + s_frequency[ch] - t_frequency[ch]
            else:
                steps = steps + s_frequency[ch]
        return steps

    def find_frequency(s):
        frequency = {}
        for ch in s:
            if ch in frequency:
                frequency[ch] = frequency[ch] + 1
            else:
                frequency[ch] = 1
        return frequency


print(Solution().minSteps("aba", "bab"))
print(Solution().minSteps("leetcode", "practice"))
