class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left_sum = [0 for _ in range(length)]
        right_sum = [0 for _ in range(length)]
        for i in range(1, length):
            left_sum[i] = nums[i-1] + left_sum[i-1]
            right_sum[length-1-i] = nums[length - i] + right_sum[length-i]
            
        return [abs(a-b) for a,b in zip(left_sum, right_sum)]
                