# https://leetcode.com/problems/counting-words-with-a-given-prefix/description /?envType=daily-question&envId=2025-01-09

from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            i = 0
            if len(pref) <= len(word):
                while i < len(pref) and pref[i] == word[i]:
                    i = i + 1

                if i == len(pref):
                    count = count + 1
        return count

    def prefixCountV2(self, words: List[str], pref: str) -> int:
        class TrieNode:
            def __init__(self):
                self.children = [None] * 26
                self.count = 0

        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insert(self, word):
                node = self.root
                for ch in word:
                    if node.children[ord(ch) - ord('a')] is None:
                        node.children[ord(ch) - ord('a')] = TrieNode()
                    node = node.children[ord(ch) - ord('a')]
                    node.count += 1

            def countPrefix(self, pref):
                node = self.root
                for ch in pref:
                    if node.children[ord(ch) - ord('a')] is not None:
                        node = node.children[ord(ch) - ord('a')]
                    else:
                        return 0
                return node.count

        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.countPrefix(pref)


print(Solution().prefixCount(
    words=["pay", "attention", "practice", "attend"], pref="at"))
print(Solution().prefixCount(
    words=["leetcode", "win", "loops", "success"], pref="code"))


print(Solution().prefixCountV2(
    words=["pay", "attention", "practice", "attend"], pref="at"))
print(Solution().prefixCountV2(
    words=["leetcode", "win", "loops", "success"], pref="code"))
