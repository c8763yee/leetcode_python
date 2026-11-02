class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = smallest2 = float('inf')
        for num in nums:
            if num <= smallest:  # Use <= to include the case when num equals smallest
                smallest = num
            elif num <= smallest2:  # Use <= here for the same reason
                smallest2 = num
            else:
                # Found a number greater than both smallest and smallest2
                return True
        return False
