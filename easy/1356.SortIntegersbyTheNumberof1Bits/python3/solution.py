class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda e: (bin(e).count('1'), e))
        return arr