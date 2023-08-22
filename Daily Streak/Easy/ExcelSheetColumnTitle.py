# https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""
        while columnNumber:
            mod = columnNumber % 26
            columnNumber = columnNumber // 26
            if mod == 0:
                columnNumber = columnNumber - 1
                mod = 26
            title = chr(mod + (ord('A') - 1)) + title
        return title

    def convertToTitleV2(self, columnNumber: int) -> str:
        title = ""
        while columnNumber:
            columnNumber = columnNumber - 1
            title = chr(columnNumber % 26 + (ord('A'))) + title
            columnNumber = columnNumber // 26
        return title


print(Solution().convertToTitle(1), Solution().convertToTitleV2(1))
print(Solution().convertToTitle(2), Solution().convertToTitleV2(2))
print(Solution().convertToTitle(3), Solution().convertToTitleV2(3))
print(Solution().convertToTitle(26), Solution().convertToTitleV2(26))
print(Solution().convertToTitle(27), Solution().convertToTitleV2(27))
print(Solution().convertToTitle(28), Solution().convertToTitleV2(28))
print(Solution().convertToTitle(29), Solution().convertToTitleV2(29))
print(Solution().convertToTitle(52), Solution().convertToTitleV2(52))
print(Solution().convertToTitle(53), Solution().convertToTitleV2(53))
print(Solution().convertToTitle(55), Solution().convertToTitleV2(55))
print(Solution().convertToTitle(254), Solution().convertToTitleV2(254))
