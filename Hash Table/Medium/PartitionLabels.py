# https://leetcode.com/problems/partition-labels/

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_indexes = {}
        i = 0
        while i < len(s):
            end_indexes[s[i]] = i
            i += 1

        partitions = []
        i = 0
        while i < len(s):
            if end_indexes[s[i]] is None:
                partitions.append(1)
            else:
                start_index = i
                end_index = end_indexes[s[i]]
                while i < end_index:
                    if end_indexes[s[i]] is not None and end_indexes[s[i]] > end_index:
                        end_index = end_indexes[s[i]]
                    i += 1
                partitions.append((end_index - start_index) + 1)
            i += 1
        return partitions


print(Solution().partitionLabels('ababcbacadefegdehijhklij'))
print(Solution().partitionLabels('eccbbbbdec'))
