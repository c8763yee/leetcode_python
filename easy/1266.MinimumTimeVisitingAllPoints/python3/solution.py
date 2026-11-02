class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]

            while x1 != x2 or y1 != y2:
                if x1 < x2:
                    x1 += 1
                elif x1 > x2:
                    x1 -= 1

                if y1 < y2:
                    y1 += 1
                elif y1 > y2:
                    y1 -= 1

                time += 1

        return time
