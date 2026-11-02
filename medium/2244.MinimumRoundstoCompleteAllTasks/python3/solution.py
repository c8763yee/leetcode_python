class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        operation_time = 0
        for value in Counter(tasks).values():
            if value == 1:
                return -1

            operation_time += math.ceil(value/3)


        return operation_time