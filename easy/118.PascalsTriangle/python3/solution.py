class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        tri.append([1])
        for i in range(1, numRows):
            arr = []
            arr.append(1)
            for j in range(1, i):
                arr.append(tri[i-1][j-1]+tri[i-1][j])
            arr.append(1)
            tri.append(arr)
            
        return tri