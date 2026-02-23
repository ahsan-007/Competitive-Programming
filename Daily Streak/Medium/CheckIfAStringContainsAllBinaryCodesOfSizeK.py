# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/?envType=daily-question&envId=2026-02-23

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        substringsSet = set()
        for i in range(len(s)-k+1):
            substringsSet.add(s[i:i+k])

        for i in range(2**k):
            binary = f"{bin(i)[2:]:0>{k}}"
            if binary not in substringsSet:
                return False
        return True

    def hasAllCodesV2(self, s: str, k: int) -> bool:
        substringsSet = set()
        for i in range(len(s)-k+1):
            substringsSet.add(s[i:i+k])
        return len(substringsSet) == 2**k

    def hasAllCodesV3(self, s: str, k: int) -> bool:
        return len({s[i:i+k] for i in range(len(s)-k+1)}) == 2**k


print(Solution().hasAllCodes(s="00110110", k=2))
print(Solution().hasAllCodes(s="0011", k=2))
print(Solution().hasAllCodes(s="0110", k=1))
print(Solution().hasAllCodes(s="0110", k=2))

print('-'*100)

print(Solution().hasAllCodesV2(s="00110110", k=2))
print(Solution().hasAllCodesV2(s="0011", k=2))
print(Solution().hasAllCodesV2(s="0110", k=1))
print(Solution().hasAllCodesV2(s="0110", k=2))
print('-'*100)

print(Solution().hasAllCodesV3(s="00110110", k=2))
print(Solution().hasAllCodesV3(s="0011", k=2))
print(Solution().hasAllCodesV3(s="0110", k=1))
print(Solution().hasAllCodesV3(s="0110", k=2))


# 1, 2, 3
# 3, 2 1

# 2
# 3    #1
