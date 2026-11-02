class Solution:
    def isValid(self, s: str) -> bool:
        part = dict(zip('({[', ')}]'))
        stack = []
        val = 0
        for c in s:
            if c in part:
                stack.append(c)
                val += 1
            elif stack and part[stack[-1]] == c:
                stack.pop()
                val -= 1
            else:
                return False

        return val == 0