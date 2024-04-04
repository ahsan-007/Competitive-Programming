# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/?envType=daily-question&envId=2024-04-04

class Solution:
    def maxDepth(self, s: str) -> int:
        maxD = 0
        depth = 0
        for ch in s:
            if ch == '(':
                depth = depth + 1
                maxD = max(maxD, depth)
            elif ch == ')':
                depth = depth - 1
        return maxD


print(Solution().maxDepth(s="(1+(2*3)+((8)/4))+1"))
print(Solution().maxDepth(s="(1)+((2))+(((3)))"))
