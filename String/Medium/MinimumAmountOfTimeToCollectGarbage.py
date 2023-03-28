# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

from typing import List


class Solution:
    # Time: O(N + M)
    # Where N is length of garbage and M is sum of lentgh of all strings in garbage
    # 1 traversal of garbage
    def garbageCollectionV2(self, garbage: List[str], travel: List[int]) -> int:
        travel_cost = 0
        pick_up_cost = 0
        current_travel_cost_G = 0
        current_travel_cost_P = 0
        current_travel_cost_M = 0
        i = -1
        for gar in garbage:
            G_found = False
            P_found = False
            M_found = False
            # for gar_type in gar:
            #     if gar_type == 'G':
            #         G_found = True
            #     elif gar_type == 'P':
            #         P_found = True
            #     else:
            #         M_found = True
            #     pick_up_cost = pick_up_cost + 1
            pick_up_cost = pick_up_cost + len(gar)
            if 'G' in gar:
                G_found = True
            if 'P' in gar:
                P_found = True
            if 'M' in gar:
                M_found = True

            if i > -1:
                current_travel_cost_G = current_travel_cost_G + travel[i]
                current_travel_cost_P = current_travel_cost_P + travel[i]
                current_travel_cost_M = current_travel_cost_M + travel[i]

            if G_found:
                travel_cost = travel_cost + current_travel_cost_G
                current_travel_cost_G = 0
            if P_found:
                travel_cost = travel_cost + current_travel_cost_P
                current_travel_cost_P = 0
            if M_found:
                travel_cost = travel_cost + current_travel_cost_M
                current_travel_cost_M = 0
            i = i + 1
        return pick_up_cost + travel_cost

    # Time: O(3N + M) -> O(N + M)
    # Where N is length of garbage and M is sum of lentgh of all strings in garbage
    # 3 traversals of garbage
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        return self.collect(garbage, travel, 'G') + self.collect(garbage, travel, 'P') + self.collect(garbage, travel, 'M')

    def collect(self, garbage, travel, type):
        travel_cost = 0
        pick_up_cost = 0
        current_travel_cost = 0
        i = -1
        for gar in garbage:
            found = False
            for gar_type in gar:
                if gar_type == type:
                    pick_up_cost = pick_up_cost + 1
                    found = True
            if i > -1:
                current_travel_cost = current_travel_cost + travel[i]
            if found:
                travel_cost = travel_cost + current_travel_cost
                current_travel_cost = 0
            i = i + 1
        return pick_up_cost + travel_cost


print(Solution().garbageCollection(
    garbage=["G", "P", "GP", "GG"], travel=[2, 4, 3]))
print(Solution().garbageCollection(
    garbage=["MMM", "PGM", "GP"], travel=[3, 10]))


print(Solution().garbageCollectionV2(
    garbage=["G", "P", "GP", "GG"], travel=[2, 4, 3]))
print(Solution().garbageCollectionV2(
    garbage=["MMM", "PGM", "GP"], travel=[3, 10]))
