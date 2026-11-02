class Solution:
    def get_height(self, red: int, blue: int) -> int:
        height = 0
        count = 1
        while True:
            flag = 0
            if blue >= count:
                height += 1
                flag = 1
            blue -= count
            count += 1

            if red >= count and flag:
                height += 1
                flag &= 1
            else:
                flag = 0
            red -= count
            count += 1

            if not flag:
                break
        return height
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        return max(self.get_height(red, blue), self.get_height(blue, red))