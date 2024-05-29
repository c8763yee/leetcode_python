#
# @lc app=leetcode id=564 lang=python3
#
# [564] Find the Closest Palindrome
#
# https://leetcode.com/problems/find-the-closest-palindrome/description/
#
# algorithms
# Hard (21.92%)
# Likes:    723
# Dislikes: 1400
# Total Accepted:    41.6K
# Total Submissions: 190K
# Testcase Example:  '"123"'
#
# Given a string n representing an integer, return the closest integer (not
# including itself), which is a palindrome. If there is a tie, return the
# smaller one.
#
# The closest is defined as the absolute difference minimized between two
# integers.
#
#
# Example 1:
#
#
# Input: n = "123"
# Output: "121"
#
#
# Example 2:
#
#
# Input: n = "1"
# Output: "0"
# Explanation: 0 and 2 are the closest palindromes but we return the smallest
# which is 0.
#
#
#
# Constraints:
#
#
# 1 <= n.length <= 18
# n consists of only digits.
# n does not have leading zeros.
# n is representing an integer in the range [1, 10^18 - 1].
#
#
#

# @lc code=start
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
        if num <= 11:
            return '9'

        prev_palindrome = next_palindrome = palindrome = 0
        high_digit = (size // 2)
        high_bit = num // (10 ** high_digit)
        palindrome = make_palindrome(high_bit, high_digit)

        if high_bit + 1 == 10 ** (high_digit + size % 2):  # 99.. -> 100..
            next_palindrome = 10 ** size + 1
            prev_palindrome = make_palindrome(high_bit, high_digit, -1)

        elif high_bit - 1 < 10 ** (high_digit - 1 + size % 2):  # 99.. -> 100..
            if num == 10 ** (size-1):
                return str(num - 1)

            prev_palindrome = 10 ** (size - 1) - 1 if high_bit - 1 > 0 else 11
            next_palindrome = make_palindrome(high_bit, high_digit, 1)
        else:
            if palindrome == num:
                prev_palindrome = make_palindrome(high_bit, high_digit, -1)
                next_palindrome = make_palindrome(high_bit, high_digit, 1)
            elif palindrome < num:
                prev_palindrome = palindrome
                next_palindrome = make_palindrome(high_bit, high_digit, 1)
            else:
                prev_palindrome = make_palindrome(high_bit, high_digit, -1)
                next_palindrome = palindrome

        return str(min(prev_palindrome, next_palindrome,
                   key=lambda x: (abs(int(x) - num), x == num, x)))
# @lc code=end
