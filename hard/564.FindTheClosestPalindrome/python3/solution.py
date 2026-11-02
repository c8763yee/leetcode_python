class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def make_palindrome(high_bit: int, high_digit: int, offset: int = 0):
            high_bit += offset if high_bit != -offset else 0
            return high_bit * (10 ** high_digit) + reverse_num(
                high_bit // (10 if size % 2 else 1))

        def reverse_num(num: int) -> int:
            rev = 0
            while num:
                rev = rev * 10 + num % 10
                num //= 10
            return rev

        size = len(n)
        if size == 1:
            return str(max(0, int(n) - 1))
        num = int(n)
        # we will see num <= 11 as special case
        if num <= 11:
            return '9'

        high_digit = (size // 2)
        high_bit = num // (10 ** high_digit)
        prev_palindrome = next_palindrome = palindrome = make_palindrome(high_bit, high_digit)

        if high_bit + 1 == 10 ** (high_digit + size % 2):  # 99.. -> 100..
            next_palindrome = 10 ** size + 1
            prev_palindrome = make_palindrome(high_bit, high_digit, -1)

        elif high_bit - 1 < 10 ** (high_digit - 1 + size % 2):  # 99.. -> 100..
            if num == 10 ** (size-1):
                return str(num - 1)

            # for 12 < n < 20, minus 1 will cause high_bit become 0, so 
            prev_palindrome = 10 ** (size - 1) - 1 if high_bit - 1 > 0 else 11
            next_palindrome = make_palindrome(high_bit, high_digit, 1)
        else:
            if palindrome <= num:
                next_palindrome = make_palindrome(high_bit, high_digit, 1)
            if palindrome >= num:
                prev_palindrome = make_palindrome(high_bit, high_digit, -1)

        return str(min(prev_palindrome, next_palindrome,
                   key=lambda x: (abs(int(x) - num), x == num, x)))