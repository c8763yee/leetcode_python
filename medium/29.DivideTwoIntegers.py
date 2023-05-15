class Solution:
    def divide(self, dividend, divisor):
        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        while dividend >= divisor:
            shift = 0
            while dividend >= (divisor << shift):
                shift += 1
            quotient += 1 << (shift - 1)
            dividend -= divisor << (shift - 1)

        if negative:
            quotient = -quotient

        return min((1<<31)-1, quotient)
