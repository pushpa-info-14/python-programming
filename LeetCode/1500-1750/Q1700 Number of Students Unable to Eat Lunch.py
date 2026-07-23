from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students:
            len_students = len(students)
            for i in range(len_students):
                if students[0] == sandwiches[0]:
                    students.pop(0)
                    sandwiches.pop(0)
                else:
                    students.append(students.pop(0))
            if len_students == len(students):
                return len_students
        return 0


s = Solution()
print(s.countStudents(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]))
print(s.countStudents(students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1]))
