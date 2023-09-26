# https://leetcode.com/problems/remove-duplicate-letters/?envType=daily-question&envId=2023-09-26

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {}
        for i in range(len(s)):
            last_index[s[i]] = i

        seen = set()
        stack = []
        for i in range(len(s)):
            if s[i] not in seen:
                while stack and s[i] <= stack[-1] and i < last_index[stack[-1]]:
                    seen.remove(stack[-1])
                    stack.pop(len(stack)-1)
                seen.add(s[i])
                stack.append(s[i])
        return ''.join(stack)


print(Solution().removeDuplicateLetters(s="bcabc"))
print(Solution().removeDuplicateLetters(s="cbacdcbc"))
