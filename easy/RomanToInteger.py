class Solution:
    def romanToInt(self, s):
        Map = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
                }
        total = 0
        size = len(s)
        for i, c in enumerate(s):
            curr = Map[c]
            total += curr
            if i == 0:
                continue
            prev = Map[s[i-1]]
            total -= prev * 2 * (prev<curr)
        return total
                
