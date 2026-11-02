class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = dict(sorted(Counter(word).items(), key=lambda pair: (-pair[1], pair[0])))

        count = 0
        for i, (k, v) in enumerate(counter.items(), start=8):
            count += i//8 * v
            
        return count
