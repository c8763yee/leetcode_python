class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        current_val = float('inf')
        for pivot, pivot_val in enumerate(nums):
            start = pivot + 1
            end = len(nums) - 1
            while start < end:
                sum_val = pivot_val + nums[start] + nums[end]
                if sum_val == target:
                    return sum_val

                if sum_val > target:
                    end -= 1
                else:
                    start += 1

                if abs(target - sum_val) < closest:
                    closest = abs(target - sum_val)
                    current_val = sum_val

        return current_val
