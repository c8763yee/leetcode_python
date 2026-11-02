from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        size = len(students)
        cnt = 0
        students = deque(students)
        sandwiches = deque(sandwiches)
        while size:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                size -= 1
                cnt = 0
            else:
                students.rotate(1)
                cnt += 1
            if cnt == size:
                return cnt
        return 0