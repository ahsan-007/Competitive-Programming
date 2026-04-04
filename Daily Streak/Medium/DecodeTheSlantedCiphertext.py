# https://leetcode.com/problems/decode-the-slanted-ciphertext/description/?envType=daily-question&envId=2026-04-04

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText

        n = len(encodedText)
        cols = n // rows
        res = []

        for c in range(cols):
            r, j = 0, c
            while r < rows and j < cols:
                res.append(encodedText[r * cols + j])
                r += 1
                j += 1

        return "".join(res).rstrip()


print(Solution().decodeCiphertext(encodedText="ch   ie   pr", rows=3))
print(Solution().decodeCiphertext(encodedText="iveo    eed   l te   olc", rows=4))
print(Solution().decodeCiphertext(encodedText="coding", rows=1))
