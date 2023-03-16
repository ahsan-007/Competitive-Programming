# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution:
    # Time: O(N), Space: O(1)
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = [False for i in range(26)]
        for ch in sentence:
            alphabets[ord(ch) - ord('a')] = True
        return not (False in alphabets)

    # Time: O(N), Space: O(1)
    # bit manipulation
    def checkIfPangramV2(self, sentence: str) -> bool:
        manip = 0
        target = (1 << 26) - 1
        for ch in sentence:
            manip = manip | 1 << ord(ch) - ord('a')
            if manip == target:
                return True
        return manip == target


print(Solution().checkIfPangram('thequickbrownfoxjumpsoverthelazydog'))
print(Solution().checkIfPangram('leetcode'))

print(Solution().checkIfPangramV2('thequickbrownfoxjumpsoverthelazydog'))
print(Solution().checkIfPangramV2('leetcode'))

# print(f"0:{(1 << 26) - 1}")
# print("{0:b}".format((1 << 26) - 1))
