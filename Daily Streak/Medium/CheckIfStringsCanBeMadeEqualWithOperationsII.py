# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/description/?envType=daily-question&envId=2026-03-30

from collections import Counter


class Solution:
    # Time: O(NlogN), Space: O(N)
    def checkStrings(self, s1: str, s2: str) -> bool:
        def sortEvenOdd(s):
            even_chars = sorted("".join(s[i] for i in range(0, len(s), 2)))
            odd_chars = sorted("".join(s[i] for i in range(1, len(s), 2)))

            i = 0
            j = 0
            formatted_s = ""
            while i < len(even_chars) or j < len(odd_chars):
                if i < len(even_chars):
                    formatted_s += even_chars[i]
                    i = i + 1

                if j < len(odd_chars):
                    formatted_s += odd_chars[j]
                    j = j + 1
            return formatted_s

        return sortEvenOdd(s1) == sortEvenOdd(s2)

    # Time: O(N), Space: O(N)
    def checkStringsV2(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])

    # Time: O(N), Space: O(1)
    def checkStringsV3(self, s1: str, s2: str) -> bool:
        freq = [0] * 52
        for i, ch in enumerate(s1):
            freq[(ord(ch) - ord('a')) + (26 if i % 2 == 1 else 0)] += 1

        for i, ch in enumerate(s2):
            freq[(ord(ch) - ord('a')) + (26 if i % 2 == 1 else 0)] -= 1

        return all(count == 0 for count in freq)


print(Solution().checkStrings(s1="abcdba", s2="cabdab"))
print(Solution().checkStrings(s1="abe", s2="bea"))

print('-'*100)

print(Solution().checkStringsV2(s1="abcdba", s2="cabdab"))
print(Solution().checkStringsV2(s1="abe", s2="bea"))

print('-'*100)

print(Solution().checkStringsV3(s1="abcdba", s2="cabdab"))
print(Solution().checkStringsV3(s1="abe", s2="bea"))
