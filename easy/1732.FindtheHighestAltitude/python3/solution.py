class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l = len(gain)
        max_val = cur = 0
        for i in range(l+1):
            if i == 0:
                continue
            cur += gain[i-1]
            max_val = max(max_val,cur )

        return max_val