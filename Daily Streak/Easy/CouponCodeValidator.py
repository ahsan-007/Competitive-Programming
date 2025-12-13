# https://leetcode.com/problems/coupon-code-validator/description/?envType=daily-question&envId=2025-12-13

from typing import List


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        filteredCoupons = []
        for i in range(len(code)):
            if isActive[i] and businessLine[i] in {"electronics", "grocery", "pharmacy", "restaurant"} and code[i]:
                couponCode = code[i].replace("_", "")
                if couponCode == "" or couponCode.isalnum():
                    filteredCoupons.append((code[i], businessLine[i]))
        filteredCoupons.sort(key=lambda x: (x[1], x[0]))
        return [code for code, _ in filteredCoupons]


print(Solution().validateCoupons(code=["SAVE20", "", "PHARMA5", "SAVE@20"], businessLine=[
      "restaurant", "grocery", "pharmacy", "restaurant"], isActive=[True, True, True, True]))
