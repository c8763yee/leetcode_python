class Solution:              
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        pairs=list(zip(difficulty, profit))
        pair_size = len(pairs)
        max_profit = 0
        numset = {}
        for k, v in pairs:
            numset[k] = max(numset.get(k, 0), v)

        difficulty.sort()
        worker.sort()
        max_profits = [0] * pair_size

        for i in range(pair_size):
            if i == 0:
                max_profits[0] = numset.get(difficulty[0], 0)
                continue
            max_profits[i] = (max(max_profits[i-1], numset.get(difficulty[i], 0)))

        j = 0
        for work in worker:
            while j < pair_size and work >= difficulty[j]:
                j += 1
            if j > 0:
                max_profit += max_profits[j-1]
        return max_profit