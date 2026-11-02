class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        area = 0
        while start < end:
            # calculate current area of water, if current area is more than max area, replace it

            hl = height[start]
            lr = height[end]

            area = max(area, (min(hl, lr)*(end-start)))
            if hl <= lr:
                start += 1
            
            if hl >= lr:
                end -= 1

        return area