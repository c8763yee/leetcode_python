class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for log in logs:
            if level != 0 and log == '../':
                level -= 1
            elif log != './' and log != '../':
                level += 1
        return level