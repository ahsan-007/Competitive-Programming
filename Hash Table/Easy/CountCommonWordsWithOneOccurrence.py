# https://leetcode.com/problems/count-common-words-with-one-occurrence/

from typing import List
from collections import Counter


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        map = {}
        for word in words1:
            if word in map:
                map[word][0] += 1
            else:
                map[word] = [1, 0]

        for word in words2:
            if word in map:
                map[word][1] += 1

        count = 0
        for key in map:
            if map[key][0] == 1 and map[key][1] == 1:
                count += 1

        return count

    def countWordsV2(self, words1: List[str], words2: List[str]) -> int:
        map1 = Counter(words1)
        map2 = Counter(words2)

        count = 0
        for word in map1:
            if map1[word] == 1 and map2.get(word, 0) == 1:
                count += 1

        return count


print(Solution().countWords(words1=[
      "leetcode", "is", "amazing", "as", "is"], words2=["amazing", "leetcode", "is"]))
print(Solution().countWords(
    words1=["b", "bb", "bbb"], words2=["a", "aa", "aaa"]))
print(Solution().countWords(words1=["a", "ab"], words2=["a", "a", "a", "ab"]))


print(Solution().countWordsV2(words1=[
      "leetcode", "is", "amazing", "as", "is"], words2=["amazing", "leetcode", "is"]))
print(Solution().countWordsV2(
    words1=["b", "bb", "bbb"], words2=["a", "aa", "aaa"]))
print(Solution().countWordsV2(
    words1=["a", "ab"], words2=["a", "a", "a", "ab"]))
