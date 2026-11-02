class Solution:
    def commonFactors(self, a: int, b: int) -> int:

        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b, a%b)

        # find GCD of a and b 
        g = gcd(a, b)

        # find prime factor of g
        factor = 1 
        for i in range(2, g+1):
            q, m = divmod(g, i)
            if m == 0:
                factor += 1
            

        return factor
        