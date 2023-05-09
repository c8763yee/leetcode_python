class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la = len(a)-1
        lb = len(b)-1
        if la == -1 or a == '0':
            return b
        if lb == -1 or b == '0':
            return a

        s = ''
        carry = 0
        while la >= 0 or lb >= 0 or carry:
            vala = 0 if la < 0 else ord(a[la]) - ord('0')
            valb = 0 if lb < 0 else ord(b[lb]) - ord('0')
            s += str((carry:=vala+valb+carry//2)%2)
            la -= 1
            lb -= 1 
        return s[-2::-1]
