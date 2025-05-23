# https://leetcode.com/problems/fizz-buzz/

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def fizzBuzzUtil(i):
            if i % 15 == 0:
                return "FizzBuzz"
            elif i % 5 == 0:
                return "Buzz"
            elif i % 3 == 0:
                return "Fizz"
            else:
                return str(i)
        return [fizzBuzzUtil(i) for i in range(1, n + 1)]


print(Solution().fizzBuzz(n=4))
print(Solution().fizzBuzz(n=5))
print(Solution().fizzBuzz(n=20))
