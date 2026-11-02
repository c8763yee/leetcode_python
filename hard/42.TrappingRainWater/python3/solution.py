class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0 
        left = 0
        right = len(height) - 1
        size = 0
        left_max = height[left]
        right_max = height[right]
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                size += left_max - height[left]

            else:
                right -= 1
                right_max = max(right_max, height[right])
                size += right_max - height[right]

        return size