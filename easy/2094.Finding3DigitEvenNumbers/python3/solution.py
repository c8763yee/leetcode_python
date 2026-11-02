class Solution:
    def comb(self, value: int = 0):
        if value >= 1000:
            return
        
        if 100 <= value < 1000 and value % 2 == 0:
            self.even.add(value)
            return

        for i, e in self.cnt.items():
            if e == 0:
                continue
            self.cnt[i] -= 1
            self.comb(value * 10 + i)
            self.cnt[i] += 1
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        self.even = set()
        self.cnt = Counter(digits)
        self.comb()
        return list(sorted(self.even))
        