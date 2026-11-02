class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a,b = (int(i) for i in num1[:-1].split('+'))
        c,d = (int(i) for i in num2[:-1].split('+'))
        return f"{a*c - b*d}+{a*d+c*b}i"