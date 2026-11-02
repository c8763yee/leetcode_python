class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maximum_good = ''
        max_val = 0
        for i in range(3, len(num)+1):
            txt = num[i-3:i]
            val = int(txt)
            if val % 111:
                continue
            if val >= max_val:
                max_val = val
                maximum_good = txt

        return maximum_good



