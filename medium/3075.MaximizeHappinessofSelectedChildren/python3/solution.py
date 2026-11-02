class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        n = len(happiness)
        happiness.sort()
        result = 0
        for i in range(k):
            c = happiness.pop() - i
            if c < 0:
                break
            result += c

        return result