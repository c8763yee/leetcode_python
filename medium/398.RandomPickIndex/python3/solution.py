class Solution:
    def __init__(self, nums: List[int]):
        self.table = {}
        for i, e in enumerate(nums):
            if e in self.table:
                self.table[e].append(i)
            else:
                self.table[e] = [i]
        

    def pick(self, target: int) -> int:
        return random.choice(self.table[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)