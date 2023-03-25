# https://leetcode.com/problems/count-items-matching-a-rule/

from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ind = {'type': 0, 'color': 1, "name": 2}
        matched_items = 0
        for item in items:
            if item[ind[ruleKey]] == ruleValue:
                matched_items = matched_items + 1
        return matched_items


print(Solution().countMatches(items=[["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], [
      "phone", "gold", "iphone"]], ruleKey="color", ruleValue="silver"))
print(Solution().countMatches(items=[["phone", "blue", "pixel"], [
      "computer", "silver", "phone"], ["phone", "gold", "iphone"]], ruleKey="type", ruleValue="phone"))
