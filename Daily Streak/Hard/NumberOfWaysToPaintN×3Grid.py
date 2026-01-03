# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/description/?envType=daily-question&envId=2026-01-03

OPTIONS = ['R', 'G', 'Y']


class Solution:
    def numOfWays(self, n: int) -> int:
        def getAllBars(options, i, currBar):
            if i >= len(options):
                return [currBar]

            bars = []
            for option in options:
                if not currBar or currBar[-1] != option:
                    bars.extend(getAllBars(options, i + 1, currBar + option))
            return bars

        def getCompatibleBars(bars):
            compatibleBars = {}
            for bar in bars:
                for currBar in bars:
                    isCompatible = True
                    k = 0
                    while k < len(currBar) and isCompatible:
                        if bar[k] == currBar[k]:
                            isCompatible = False
                        k = k + 1

                    if isCompatible:
                        if currBar not in compatibleBars:
                            compatibleBars[currBar] = []
                        compatibleBars[currBar].append(bar)
            return compatibleBars

        allBars = getAllBars(OPTIONS, 0, '')
        compatibleBars = getCompatibleBars(allBars)

        memo = {}

        def numWaysUtil(compatibleBars, currBar, i, n):
            if i == n:
                return 0

            if i == n - 1:
                return len(compatibleBars[currBar]) if i != 0 else 12

            if (currBar, i) in memo:
                return memo[(currBar, i)]

            count = 0
            bars = list(compatibleBars.keys()
                        ) if i == 0 else compatibleBars[currBar]
            for bar in bars:
                count = count + numWaysUtil(compatibleBars, bar, i + 1, n)
            memo[(currBar, i)] = count
            return count

        return numWaysUtil(compatibleBars, None, 0, n) % (pow(10, 9) + 7)

    def numOfWaysV2(self, n: int) -> int:
        A = 6  # patterns like RGR where row starts and ends with the same color
        B = 6  # patterns like RGY where all colors are unique
        for i in range(2, n + 1):
            A, B = 2 * A + 2 * B, 2 * A + 3 * B
        return (A + B) % (pow(10, 9) + 7)
    

print(Solution().numOfWays(n=1))
print(Solution().numOfWays(n=2))
print(Solution().numOfWays(n=3))
print(Solution().numOfWays(n=4))
print(Solution().numOfWays(n=5))
print(Solution().numOfWays(n=50))

print('-' * 100)

print(Solution().numOfWaysV2(n=1))
print(Solution().numOfWaysV2(n=2))
print(Solution().numOfWaysV2(n=3))
print(Solution().numOfWaysV2(n=4))
print(Solution().numOfWaysV2(n=5))
print(Solution().numOfWaysV2(n=50))
