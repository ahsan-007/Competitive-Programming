# https://leetcode.com/problems/push-dominoes/description/?envType=daily-question&envId=2025-05-02

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        finalState = ""
        dots = 0
        right = False
        for domino in dominoes:
            if domino == ".":
                dots = dots + 1

            elif domino == "L":
                if right:
                    finalState = finalState + "R" * (dots//2)
                    if dots % 2 == 1:
                        finalState = finalState + "."
                    finalState = finalState + "L" * (dots//2 + 1)

                    right = False
                else:
                    finalState = finalState + "L" * (dots + 1)

                dots = 0
            else:
                if right:
                    finalState = finalState + "R" * dots

                elif dots > 0:
                    finalState = finalState + "." * dots

                finalState = finalState + "R"
                right = True
                dots = 0

        if dots > 0:
            if right:
                finalState = finalState + "R" * dots
            else:
                finalState = finalState + "." * dots

        return finalState


print(Solution().pushDominoes(dominoes="RR.L"))
print(Solution().pushDominoes(dominoes=".L.R...LR..L.."))
print(Solution().pushDominoes(dominoes="R...L"))
print(Solution().pushDominoes(dominoes=".L.R"))
print(Solution().pushDominoes(dominoes=".L.R."))
