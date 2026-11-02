class Solution:
    def customSortString(self, order: str, s: str) -> str:
        maps = dict(zip(order, range(len(order))))
        return ''.join(sorted(s, key=lambda x:maps.get(x, 2 ** 31 - 1)))