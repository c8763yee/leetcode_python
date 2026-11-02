class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alpha = list(map(chr, range(65, 91)))  # A-Z
        s = []
        while columnNumber > 0:
            columnNumber -= 1
            s.append(alpha[columnNumber % 26])
            columnNumber //= 26

        s.reverse()
        return ''.join(s)
