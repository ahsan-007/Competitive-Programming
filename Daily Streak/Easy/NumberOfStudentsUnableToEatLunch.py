# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description /?envType=daily-question&envId=2024-04-08

from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = 0
        noOfStudentsUnableToEat = 0
        while i < len(sandwiches) and noOfStudentsUnableToEat < len(students):
            if sandwiches[i] != students[0]:
                students.append(students.pop(0))
                noOfStudentsUnableToEat = noOfStudentsUnableToEat + 1
            else:
                students.pop(0)
                noOfStudentsUnableToEat = 0
                i = i + 1
        return noOfStudentsUnableToEat

    def countStudentsV2(self, students: List[int], sandwiches: List[int]) -> int:
        squareStudents = 0
        circleStudents = 0
        for student in students:
            if student == 0:
                circleStudents += 1
            else:
                squareStudents += 1

        for sandwich in sandwiches:
            if sandwich == 0:
                if circleStudents == 0:
                    return squareStudents
                else:
                    circleStudents -= 1

            if sandwich == 1:
                if squareStudents == 0:
                    return circleStudents
                else:
                    squareStudents -= 1
        return 0


print(Solution().countStudents(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]))
print(Solution().countStudents(
    students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1]))

print('-' * 100)

print(Solution().countStudentsV2(
    students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]))
print(Solution().countStudentsV2(
    students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1]))
