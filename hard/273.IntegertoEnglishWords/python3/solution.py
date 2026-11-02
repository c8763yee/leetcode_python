method = ["", " Thousand", " Million", " Billion"]
num_mapping = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety",
}


class Solution:
    def num_to_words(self, num, level=0):
        words = ""
        if num >= 1000:
            words = f"{self.num_to_words(num // 1000, level+1)}"
            num %= 1000
            if num == 0:
                return words

        if num >= 100:
            if words:
                words += ' '
            
            words += f"{num_mapping[num//100]} Hundred"
            num %= 100

        if num == 0:
            return (words + method[level]).strip()

        if words:
            words += ' '
        if num in num_mapping:
            return words + f"{num_mapping[num]}{method[level]}"

        digit = num % 10
        return (
            words + f"{num_mapping[num-digit]} {num_mapping[digit]}{method[level]}"
        )

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        return self.num_to_words(num)
