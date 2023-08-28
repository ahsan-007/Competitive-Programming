# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whiteBlocks = 0
        i = 0
        while i < k:
            if blocks[i] == 'W':
                whiteBlocks += 1
            i = i + 1

        minOperations = whiteBlocks
        while i < len(blocks) and minOperations != 0:
            if blocks[i] == 'W' and blocks[i-k] != 'W':
                whiteBlocks += 1

            elif blocks[i] == 'B' and blocks[i-k] == 'W':
                whiteBlocks -= 1

            minOperations = min(minOperations, whiteBlocks)
            i = i + 1
        return minOperations


print(Solution().minimumRecolors(blocks="WBBWWBBWBW", k=7))
print(Solution().minimumRecolors(blocks="WBWBBBW", k=2))
