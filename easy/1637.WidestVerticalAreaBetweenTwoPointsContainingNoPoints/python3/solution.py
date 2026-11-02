class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        max_diff = 0
        for i in range(1, len(points)):
            x = points[i][0]
            max_diff = max(max_diff, x - points[i-1][0])
        return max_diff