# https://leetcode.com/problems/count-and-say/description/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        say = self.countAndSay(n - 1)
        result = ""
        count = 0
        dig = ""
        i = 0
        while i < len(say):
            if dig != say[i]:
                if dig != "":
                    result = result + str(count) + dig
                dig = say[i]
                count = 1
            else:
                count = count + 1
            i = i + 1
        result = result + str(count) + dig
        return result


print(Solution().countAndSay(1))
print(Solution().countAndSay(2))
print(Solution().countAndSay(3))
print(Solution().countAndSay(4))
print(Solution().countAndSay(30))
