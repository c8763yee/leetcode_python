class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        r = len(original)
        if r != m*n:
            return []
        if m == 1:
            return [original]
        if n == 1:
            return [[i] for i in original]
        mat = [[0 for _ in range(n)] for _ in range(m)]
        for i, e in enumerate(original):
            mat[i//n][i%n] = e


        return mat