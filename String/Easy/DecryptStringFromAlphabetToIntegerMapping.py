# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        decrypted_str = ""
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == '#':
                num = int(s[i:i+2])
                i = i + 3
            else:
                num = int(s[i])
                i = i + 1
            decrypted_str = decrypted_str + chr(ord('a') + (num - 1))
        return decrypted_str
    
    
print(Solution().freqAlphabets(s = "10#11#12"))
print(Solution().freqAlphabets(s = "1326#"))
