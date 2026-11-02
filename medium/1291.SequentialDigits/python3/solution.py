def get_digit(num: int) -> int:
    x = 0
    while num:
        x += 1
        num //= 10
    return x


def start_digit(end: int) -> int:
    start = 1
    digit = 1
    for _ in range(end - 1):
        digit += 1
        start *= 10
        start += digit
    return start


def get_diff(end: int) -> int:
    digit = 1
    for _ in range(end - 1):
        digit *= 10
        digit += 1
    return digit


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        result = []
        for digit in range(get_digit(low), get_digit(high) + 1):
            val = start_digit(digit)
            diff = get_diff(digit)
            while val % 10 != 0:
                if val > high:
                    return result
                elif val >= low:
                    result.append(val)
                val += diff

        return result
