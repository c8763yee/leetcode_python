class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join([c*e for c, e in sorted(Counter(s).items(),key=lambda a: a[1],reverse=True)])