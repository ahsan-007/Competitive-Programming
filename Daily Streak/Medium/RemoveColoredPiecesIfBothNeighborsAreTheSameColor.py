# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/description/?envType=daily-question&envId=2023-10-02

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_turns = bob_turns = 0
        i = 1
        while i < len(colors) - 1:
            if colors[i-1] == colors[i] and colors[i] == colors[i+1]:
                if colors[i] == 'A':
                    alice_turns = alice_turns + 1
                else:
                    bob_turns = bob_turns + 1
            i = i + 1
        return alice_turns > bob_turns


print(Solution().winnerOfGame(colors="AAABABB"))
print(Solution().winnerOfGame(colors="AA"))
print(Solution().winnerOfGame(colors="ABBBBBBBAAA"))
print(Solution().winnerOfGame(colors="AAAAABBB"))
