class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet = set()
        size = len(nums)
        nums.sort()
        for pivot in range(size - 2):
            left = pivot + 1
            right = size - 1
            while left < right:
                sum_val = nums[pivot] + nums[left] + nums[right]
                if sum_val == 0:
                    triplet.add((nums[pivot], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    continue

                elif sum_val < 0:
                    left += 1
                else:
                    right -= 1

        return triplet