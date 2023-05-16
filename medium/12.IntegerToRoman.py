class Solution:
    def intToRoman(self, num):
        if num<4:
            return 'I' * num
        s = ''
        dic = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        for val, roman in dic.items():
            if num < val:
                continue
            s += roman * (num//val)
            num %= val
        return s
