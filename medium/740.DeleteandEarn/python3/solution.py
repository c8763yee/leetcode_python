class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ptr = sorted(counter.keys())
        prev, curr = 0, 0
        for i, k in enumerate(ptr):
            current_points = k * counter[k]
            if i > 0 and k == ptr[i - 1] + 1:
                prev, curr = curr, max(curr, prev + current_points)
            else:
                prev, curr = curr, curr + current_points

        return curr
