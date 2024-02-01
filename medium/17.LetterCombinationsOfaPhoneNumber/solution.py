class Solution:
    def letterCombinations(self, digits):
        table = {
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'
            }
        letters = []
        comb = []
        def makeComb(idx=0):
            if idx == len(digits):
                comb.append(''.join(letters))
                return
            for i in table[digits[idx]]:
                letters.append(i)
                makeComb(idx+1)
                letters.pop()

        if not digits:
            return []
        makeComb()
        return comb
