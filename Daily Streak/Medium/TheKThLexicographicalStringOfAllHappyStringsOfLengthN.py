# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/editorial/?envType=daily-question&envId=2026-03-14

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (1 << (n - 1))

        if k > total:
            return ""

        result = ["a"] * n

        next_smallest = {"a": "b", "b": "a", "c": "a"}
        next_greatest = {"a": "c", "b": "c", "c": "b"}

        start_a = 1
        start_b = start_a + (1 << (n - 1))
        start_c = start_b + (1 << (n - 1))

        if k < start_b:
            result[0] = "a"
            k = k - start_a
        elif k < start_c:
            result[0] = "b"
            k = k - start_b
        else:
            result[0] = "c"
            k = k - start_c

        for char_index in range(1, n):
            midpoint = 1 << (n - char_index - 1)

            if k < midpoint:
                result[char_index] = next_smallest[result[char_index - 1]]
            else:
                result[char_index] = next_greatest[result[char_index - 1]]
                k = k - midpoint

        return "".join(result)


print(Solution().getHappyString(n=1, k=3))
print(Solution().getHappyString(n=1, k=4))
print(Solution().getHappyString(n=3, k=9))
