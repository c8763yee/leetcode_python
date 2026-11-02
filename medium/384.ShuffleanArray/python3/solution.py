class Solution:
    def __init__(self, nums: List[int]):
        self.arr = nums
        self.orr_arr = nums[::]
        self.size = len(self.arr)

    def reset(self) -> List[int]:
        return self.orr_arr

    def shuffle(self) -> List[int]:
        for i in range(self.size):
            j = random.randrange(self.size)
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        return self.arr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()