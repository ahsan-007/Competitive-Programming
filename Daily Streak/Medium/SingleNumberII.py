# https://leetcode.com/problems/single-number-ii/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        positive_bits = [0 for i in range(32)]
        negative_bits = [0 for i in range(32)]
        for num in nums:
            binary = bin(num)[(3 if num < 0 else 2):]
            j = 31
            for i in range(len(binary)-1, -1, -1):
                if binary[i] == '1':
                    if num < 0:
                        negative_bits[j] = negative_bits[j] + 1
                    else:
                        positive_bits[j] = positive_bits[j] + 1
                j = j - 1

        is_negative = True
        for i in range(32):
            negative_bits[i] = str(negative_bits[i] % 3)
            positive_bits[i] = str(positive_bits[i] % 3)
            if positive_bits[i] == '1':
                is_negative = False

        return -int(''.join(negative_bits), 2) if is_negative else int(''.join(positive_bits), 2)


print(Solution().singleNumber(nums=[2, 2, 2, 3]))
print(Solution().singleNumber(nums=[0, 1, 0, 1, 0, 1, 3]))
print(Solution().singleNumber(nums=[0, 0, 1, 0, 1, 1, 3, 2, 3, -6, 3, 2, 2]))

# print(bin(-6))
