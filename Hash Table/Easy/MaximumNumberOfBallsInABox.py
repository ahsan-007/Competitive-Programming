# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}
        for i in range(lowLimit, highLimit+1):
            box_number = self.get_box_number(i)
            if box_number in boxes:
                boxes[box_number] = boxes[box_number] + 1
            else:
                boxes[box_number] = 1
        max_balls = boxes[list(boxes.keys())[0]]
        for key in boxes:
            max_balls = max(max_balls, boxes[key])
        return max_balls

    def get_box_number(self, num):
        box_number = 0
        while num > 0:
            box_number = box_number + num % 10
            num = num // 10
        return box_number


print(Solution().countBalls(1, 10))
print(Solution().countBalls(5, 15))
print(Solution().countBalls(19, 28))


# Input: lowLimit = 1, highLimit = 10
# Output: 2
# Explanation:
# Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
# Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
# Box 1 has the most number of balls with 2 balls.
# Example 2:

# Input: lowLimit = 5, highLimit = 15
# Output: 2
# Explanation:
# Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
# Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
# Boxes 5 and 6 have the most number of balls with 2 balls in each.
# Example 3:

# Input: lowLimit = 19, highLimit = 28
# Output: 2
# Explanation:
# Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ...
# Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ...
# Box 10 has the most number of balls with 2 balls.
