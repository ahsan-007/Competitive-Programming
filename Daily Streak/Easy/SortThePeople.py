# https://leetcode.com/problems/sort-the-people/description /?envType=daily-question&envId=2024-07-22

from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        def merge_sort(names, heights):
            def merge(names1, heights1, names2, heights2):
                merged_heights = [0] * (len(heights1) + len(heights2))
                merged_names = [0] * (len(names1) + len(names2))

                i = j = k = 0
                while i < len(heights1) or j < len(heights2):
                    if i < len(heights1) and j < len(heights2):
                        if heights1[i] > heights2[j]:
                            merged_heights[k], merged_names[k] = heights1[i], names1[i]
                            i = i + 1
                        else:
                            merged_heights[k], merged_names[k] = heights2[j], names2[j]
                            j = j + 1

                    elif i < len(heights1):
                        merged_heights[k], merged_names[k] = heights1[i], names1[i]
                        i = i + 1
                    else:
                        merged_heights[k], merged_names[k] = heights2[j], names2[j]
                        j = j + 1
                    k = k + 1
                return merged_names, merged_heights

            if len(heights) == 1:
                return names, heights

            mid = len(heights) // 2
            names1, heights1 = merge_sort(names[0:mid], heights[0:mid])
            names2, heights2 = merge_sort(
                names[mid:len(names)], heights[mid:len(heights)])
            return merge(names1, heights1, names2, heights2)

        names, _ = merge_sort(names, heights)
        return names


print(Solution().sortPeople(
    names=["Mary", "John", "Emma"], heights=[180, 165, 170]))
