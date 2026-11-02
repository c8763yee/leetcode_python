def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)        

def lcm(a, b):
    return a * b  // gcd(a, b)

class Solution:
    def fractionAddition(self, expression: str) -> str:
        spliter = []
        current_lcm = 1
        prev = expression[0] == '+'
        for i, e in enumerate(expression):
            if i == 0 or not (e == '-' or e == '+'):
                continue

            exp = tuple(map(int, expression[prev:i].split('/')))
            spliter.append(exp)
            prev = (i+(e!='-'))
            current_lcm = lcm(current_lcm, exp[1])
            
        tail_exp = tuple(map(int, expression[prev:].split("/")))
        spliter.append(tail_exp)
        current_lcm = lcm(current_lcm, tail_exp[1])
        
        total_num = 0
        for i, (num, den) in enumerate(spliter):
            spliter[i] = (num * current_lcm // den, current_lcm)
            total_num += spliter[i][0]

        if total_num == 0:
            return "0/1"

        base = gcd(total_num, current_lcm)
        final_num = total_num // base
        final_den = current_lcm // base
        return f"{final_num}/{final_den}"