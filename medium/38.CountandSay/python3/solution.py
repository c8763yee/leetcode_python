class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        table = []
        prev = ''
        cnt = 1
        s = self.countAndSay(n-1)
        for k in s:
            if prev == '':
                prev = k
                continue
            if prev == k:
                cnt += 1
                continue
            table.append(str(cnt)+prev)
            cnt = 1
            prev = k
        if prev == s[-1]:
            table.append(str(cnt)+k)
        return ''.join(table)
    