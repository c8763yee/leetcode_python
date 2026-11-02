class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        dimensions.sort(key=lambda pair: (pow(pair[0]*pair[0]+pair[1]*pair[1], 0.5), pair[0]*pair[1]))
        
        
        a, b = dimensions[-1]
        return a*b