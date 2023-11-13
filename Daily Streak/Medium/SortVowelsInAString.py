# https://leetcode.com/problems/sort-vowels-in-a-string/description/?envType=daily-question&envId=2023-11-13

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')
        vowelsFreq = {}

        for ch in s:
            if ch in vowels:
                vowelsFreq[ch] = vowelsFreq.get(ch, 0) + 1

        i = 0
        while i < len(s) and vowelsFreq:
            if s[i] in vowels:
                j = 0
                found = False
                while j < len(vowels) and not found:
                    if vowelsFreq.get(vowels[j], 0) > 0:
                        s = s[:i] + vowels[j] + s[i+1:]
                        found = True
                        vowelsFreq[vowels[j]] = vowelsFreq[vowels[j]] - 1
                        if vowelsFreq[vowels[j]] == 0:
                            del vowelsFreq[vowels[j]]
                    j = j + 1
            i = i + 1
        return s


print(Solution().sortVowels(s="lEetcOde"))
print(Solution().sortVowels(s="lYmpH"))
