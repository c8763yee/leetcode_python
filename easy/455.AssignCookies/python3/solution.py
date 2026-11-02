class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if s == []:
            return 0

        g.sort()
        s.sort()
        count = 0
        child_pointer = 0
        for cookie_pointer, cookie in enumerate(s):
            if g[child_pointer] <= cookie: # suitable
                count += 1
                child_pointer += 1
                if child_pointer == len(g):
                    break
            cookie_pointer += 1

        return max(count, 1)
