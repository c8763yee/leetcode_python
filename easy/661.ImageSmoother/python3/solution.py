from itertools import product
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        col = len(img[0])
        new_img = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                current = 0
                div = 9
                for inner_i, inner_j in product(range(-1, 2),range(-1, 2)):
                    flag = False
                    # print(inner_i, inner_j, inner)
                    if (j + inner_j >= col) or (j + inner_j < 0):
                        div -= 1
                        flag = True
                    if (i + inner_i) >= row or (i + inner_i < 0):
                        div -= not flag
                        flag = True
                    if flag:
                        continue
                    current += img[i+inner_i][j+inner_j]
                new_img[i][j] = current // div

        return new_img
                        