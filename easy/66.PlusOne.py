class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits[-1] += 1
        length = len(digits)
        for i in range(length):
            if digits[length - i - 1] == 10:
                digits[length - i - 1] = 0
                if i == length - 1:
                    return [1] + digits
                digits[length - i - 2] += 1

        if digits[0] == 0:
            digits.pop(0)
        return digits
