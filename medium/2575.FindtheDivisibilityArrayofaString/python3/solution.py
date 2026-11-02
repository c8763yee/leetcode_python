class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        lst = []
        sum_ = 0
        for i in word:
            sum_ = (sum_ * 10 + int(i))%m
            lst.append(sum_==0 and 1 or 0)
        return lst