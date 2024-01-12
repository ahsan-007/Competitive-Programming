# https://leetcode.com/problems/determine-if-string-halves-are-alike/description/?envType=daily-question&envId=2024-01-12

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half_length = len(s) // 2
        count = 0
        for i in range(half_length):
            if s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
                count = count + 1

            if s[i + half_length].lower() in ['a', 'e', 'i', 'o', 'u']:
                count = count - 1

        return count == 0


print(Solution().halvesAreAlike("book"))
print(Solution().halvesAreAlike("textbook"))
