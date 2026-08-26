# https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/description/?envType=daily-question&envId=2026-08-26

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        i = 0
        j = 0
        ones = 0
        shortest_beautiful_string = None
        while j < len(s) or ones == k:
            if ones == k:
                if s[i] == "1":
                    ones -= 1
                i = i + 1

            else:
                if s[j] == "1":
                    ones += 1
                j += 1

            if ones == k:
                if (shortest_beautiful_string is None or
                    (j - i) < len(shortest_beautiful_string) or
                        ((j-i) == len(shortest_beautiful_string) and s[i:j] < shortest_beautiful_string)):
                    shortest_beautiful_string = s[i:j]
        return shortest_beautiful_string if shortest_beautiful_string else ""


print(Solution().shortestBeautifulSubstring(s="100011001", k=3))
print(Solution().shortestBeautifulSubstring(s="1011", k=2))
print(Solution().shortestBeautifulSubstring(s="000", k=1))
print(Solution().shortestBeautifulSubstring(
    s="1100100101011001001", k=7))
