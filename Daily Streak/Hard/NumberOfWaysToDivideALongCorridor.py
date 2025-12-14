# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/description/?envType=daily-question&envId=2025-12-14

class Solution:
    # Time: O(N), Space: O(1)
    def numberOfWays(self, corridor: str) -> int:
        SEATS_BETWEEN_DIVIDERS = 2
        ways = 0
        plants = 0
        seats = 0
        for i in range(len(corridor)):
            if corridor[i] == "S":
                if seats == SEATS_BETWEEN_DIVIDERS:
                    if plants > 0:
                        if ways == 0:
                            ways = plants + 1
                        else:
                            ways = ways * (plants + 1)
                        plants = 0
                    seats = 1
                else:
                    seats += 1
            # only the plants that are between 2 pair of seats matter
            elif corridor[i] == "P" and seats == SEATS_BETWEEN_DIVIDERS:
                plants += 1

        if seats == SEATS_BETWEEN_DIVIDERS and ways == 0:
            return 1

        return 0 if seats == 1 else (ways % ((10**9)+7))


print(Solution().numberOfWays(corridor="SSPPSPS"))
print(Solution().numberOfWays(corridor="PPSPSP"))
print(Solution().numberOfWays(corridor="S"))
print(Solution().numberOfWays(corridor="SSPPSSPPSS"))
print(Solution().numberOfWays(corridor="P"))
print(Solution().numberOfWays(corridor="SPPSSSSPPS"))
