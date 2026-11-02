class Solution:
    def countBits(self, n: int) -> List[int]:
        memory = [0 for _ in range(n + 1)]
        sub = 1
        for i in range(1, n + 1):
            if sub * 2 == i:
                sub = i

            memory[i] = memory[i - sub] + 1

        return memory

