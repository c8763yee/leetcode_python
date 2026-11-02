class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        for c in s:
            if c == '#' and stack_s:
                stack_s.pop()
            elif c != '#':
                stack_s.append(c)

        for c in t:
            if c == '#' and stack_t:
                stack_t.pop()
            elif c != '#':
                stack_t.append(c)

        return stack_s == stack_t
