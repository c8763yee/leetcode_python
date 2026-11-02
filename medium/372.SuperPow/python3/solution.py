class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        a %= 1337
        if a <= 1:
            return a
        
        pow_val = 0
        x = 1
        mod = 1337

        power = a % mod
        for i in b:
            pow_val = pow_val * 10 + i

        for pow_flag in bin(pow_val)[:1:-1]:
            if pow_flag == '1':
                x = (x * power) % mod
            
            power = (power*power) % mod
        return x