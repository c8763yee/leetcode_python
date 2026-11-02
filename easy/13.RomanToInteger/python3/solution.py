class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}

        value = roman[s[0]]
        for i, c in enumerate(s):
            if i == 0:
                continue

            value += -2 * roman[s[i-1]] * (roman[s[i-1]] < roman[c]) + roman[c]

        return value