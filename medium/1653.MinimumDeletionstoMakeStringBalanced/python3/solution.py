class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = []
        b_before = 0
        a_after = s.count('a')

        for c in s:
            if c == 'a':
                a_after -= 1

            dp.append(b_before + a_after)

            if c == 'b':
                b_before += 1

        
        return min(dp)