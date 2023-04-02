# https://leetcode.com/problems/count-asterisks/

class Solution:
    def countAsterisks(self, s: str) -> int:
        bar = False
        count = 0
        for ch in s:
            if ch == '*':
                if not bar:
                    count = count + 1
            elif ch == '|':
                bar = not bar
        return count


print(Solution().countAsterisks(s="l|*e*et|c**o|*de|"))
print(Solution().countAsterisks(s="iamprogrammer"))
print(Solution().countAsterisks(s="yo|uar|e**|b|e***au|tifu|l"))
