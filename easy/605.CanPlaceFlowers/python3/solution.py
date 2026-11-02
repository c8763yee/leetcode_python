class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        if l == 1:
            return n == 0 or flowerbed[0] == 0
        for i, e in enumerate(flowerbed):
            if n == 0:
                return True
            if e == 1:
                continue

            if flowerbed[-2] == 0 and i == l - 1 or i == 0 and flowerbed[1] == 0:
                flowerbed[i] = 1
                n -= 1

            elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1

        return n <= 0