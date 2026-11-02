class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for arg in range(i+1):
                if arg == 0 or i == 1:
                    triangle[i][arg] += triangle[i-1][0]
                elif arg == i:
                    triangle[i][arg] += triangle[i-1][-1]
                else:
                    triangle[i][arg] += min(triangle[i-1][arg], triangle[i-1][arg-1])
        return min(triangle[-1])