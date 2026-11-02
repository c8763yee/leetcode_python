class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda pair: -pow(pair[0]*pair[0]+pair[1]*pair[1], 0.5))
        return points[-1:-k-1:-1]