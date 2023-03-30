# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if len(stack) == 0 or stack[-1] != ch:
                stack.append(ch)
            else:
                while len(stack) > 0 and stack[-1] == ch:
                    stack.pop()
        return ''.join(stack)


print(Solution().removeDuplicates('abbaca'))
print(Solution().removeDuplicates('azxxzy'))
