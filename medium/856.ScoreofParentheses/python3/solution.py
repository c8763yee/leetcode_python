class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        arr = []
        for c in s:
            val = 0
            if c == '(':
                arr.append(c)
                continue
            while arr:
                if arr[-1] == '(':
                    arr[-1] = 1 if val == 0 else 2 * val
                    break
                val += arr.pop()
        return sum(arr)
