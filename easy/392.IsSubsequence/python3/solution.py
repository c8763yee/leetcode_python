class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        if t == '':
            return False
        ptr = 0
        s_len = len(s)
        t_len = len(t)
        for i, c in enumerate(t):
            if c == s[ptr]:
                ptr += 1
            if ptr == s_len:
                return True


        return False