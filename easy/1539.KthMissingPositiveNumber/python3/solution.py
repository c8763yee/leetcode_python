class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # O(n) solution
        idx = 0
        for i in range(1, 1+arr[-1]):
            if i == arr[idx]:
                idx += 1
                continue
            k -= 1
            if k == 0:
                return i
        return arr[-1]+k