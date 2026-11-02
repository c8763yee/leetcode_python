#import numpy as np
class Solution:
    
    # using numpy:367ms Runtime and 32.6MB memory
    # def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    #     mat = np.array(mat)
    #     i, j = mat.shape
    #     return mat if r*c != i*j else mat.reshape(r, c)
    
    
    #without using numpy:99ms Runtime and 14.6MB memory
    def get_shape(self, arr):
        return map(len, [arr, arr[0]])
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        i, j = self.get_shape(mat)
        if i*j != r*c:
            return mat
        print(i, j, r, c)
        new = [[0 for _ in range(c)] for _ in range(r)]
        for x in range(r*c):
            new[x//c][x%c] = mat[x//j][x%j]
        
        return new
    
    