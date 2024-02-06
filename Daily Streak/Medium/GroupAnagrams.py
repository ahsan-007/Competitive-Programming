# https://leetcode.com/problems/group-anagrams/description/

from typing import List
from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        for i in range(len(strs)):
            strs[i] = {
                'word': strs[i],
                'sorted': ''.join(sorted(strs[i]))
            }

        anagrams = []
        i = 0
        while i < len(strs):
            if strs[i] is not None:
                current_anagrams = [strs[i]['word']]
                j = i + 1
                while j < len(strs):
                    if strs[j] is not None and strs[i]['sorted'] == strs[j]['sorted']:
                        current_anagrams.append(strs[j]['word'])
                        strs[j] = None
                    j = j + 1
                strs[i] = None
                anagrams.append(current_anagrams)
            i = i + 1

        return anagrams

    def groupAnagramsV2(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)

        return [anagrams[word] for word in anagrams]

    def groupAnagramsV3(self, strs: List[str]) -> List[List[str]]:
        def getSignature(s):
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1

            signature = ""
            for ind in range(len(count)):
                if count[ind] != 0:
                    signature = signature + \
                        chr(ord('a') + ind) + str(count[ind])
            return signature

        anagrams = {}
        for word in strs:
            signature = getSignature(word)
            if signature not in anagrams:
                anagrams[signature] = []
            anagrams[signature].append(word)

        return [anagrams[word] for word in anagrams]


print(Solution().groupAnagrams(
    strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().groupAnagrams(strs=[""]))
print(Solution().groupAnagrams(strs=["", ""]))
print(Solution().groupAnagrams(strs=["a"]))
print(Solution().groupAnagrams(strs=["c", "c"]))
print(Solution().groupAnagrams(strs=["", "b", ""]))

print('-'*100)

print(Solution().groupAnagramsV2(
    strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().groupAnagramsV2(strs=[""]))
print(Solution().groupAnagramsV2(strs=["", ""]))
print(Solution().groupAnagramsV2(strs=["a"]))
print(Solution().groupAnagramsV2(strs=["c", "c"]))
print(Solution().groupAnagramsV2(strs=["", "b", ""]))

print('-'*100)

print(Solution().groupAnagramsV3(
    strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().groupAnagramsV3(strs=[""]))
print(Solution().groupAnagramsV3(strs=["", ""]))
print(Solution().groupAnagramsV3(strs=["a"]))
print(Solution().groupAnagramsV3(strs=["c", "c"]))
print(Solution().groupAnagramsV3(strs=["", "b", ""]))
