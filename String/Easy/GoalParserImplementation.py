# https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        interpretation = ''
        while i < len(command):
            if command[i] == 'G':
                interpretation = interpretation + 'G'
                i = i + 1
            elif command[i:i+2] == '()':
                interpretation = interpretation + 'o'
                i = i + 2
            else:
                interpretation = interpretation + 'al'
                i = i + 4
        return interpretation


print(Solution().interpret('G()(al)'))
print(Solution().interpret('G()()()()(al)'))
print(Solution().interpret('(al)G(al)()()G'))
