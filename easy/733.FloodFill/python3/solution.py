class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        def fill(r, c, color, target):
            if not (
                0 <= r < len(image) and
                0 <= c < len(image[0])
            ):
                return

            if image[r][c] != target:
                return

            image[r][c] = color
            fill(r-1, c, color, target)
            fill(r+1, c, color, target)
            fill(r, c-1, color, target)
            fill(r, c+1, color, target)

        fill(sr, sc, color, image[sr][sc])
        return image