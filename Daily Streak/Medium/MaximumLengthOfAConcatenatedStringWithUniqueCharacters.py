# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/?envType=daily-question&envId=2024-01-23

from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def maxLengthUtil(arr, i, characters):
            if i == len(arr):
                return 0

            uniqueCharacters = True
            j = 0
            while j < len(arr[i]) and uniqueCharacters:
                if arr[i][j] in characters:
                    uniqueCharacters = False
                else:
                    characters.add(arr[i][j])
                    j = j + 1

            maximumLength = 0
            if uniqueCharacters:
                maximumLength = len(arr[i]) + \
                    maxLengthUtil(arr, i+1, characters)

            j = j - 1
            while j >= 0:
                characters.remove(arr[i][j])
                j = j - 1

            return max(maximumLength, maxLengthUtil(arr, i+1, characters))

        return maxLengthUtil(arr, 0, set())

    def maxLengthV2(self, arr: List[str]) -> int:
        def binary_representation(word):
            binary = 0
            for ch in word:
                binary = binary | (1 << (ord(ch) - ord('a')))
            return binary

        def maxLengthUtil(binary_representations, i, current_binary):
            if i == len(binary_representations):
                return bin(current_binary).count("1")

            maxLength = 0
            if current_binary & binary_representations[i] == 0:
                maxLength = maxLengthUtil(binary_representations, i + 1,
                                          current_binary | binary_representations[i])

            return max(maxLength, maxLengthUtil(binary_representations, i + 1, current_binary))

        i = 0
        while i < len(arr):
            if len(arr[i]) != len(set(arr[i])):
                arr.pop(i)
            else:
                i = i + 1

        binary_representations = [binary_representation(word) for word in arr]

        return maxLengthUtil(binary_representations, 0, 0)


print(Solution().maxLength(arr=["un", "iq", "ue"]))
print(Solution().maxLength(arr=["cha", "r", "act", "ers"]))
print(Solution().maxLength(arr=["abcdefghijklmnopqrstuvwxyz"]))

print(Solution().maxLengthV2(arr=["un", "iq", "ue"]))
print(Solution().maxLengthV2(arr=["cha", "r", "act", "ers"]))
print(Solution().maxLengthV2(arr=["abcdefghijklmnopqrstuvwxyz"]))
