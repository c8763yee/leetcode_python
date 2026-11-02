class Solution:
    def minOperations(self, s: str) -> int:
        count = 0

        # 101010
        for i, c in enumerate(s):
            count += (i&1 and c == '0' or i%2 == 0 and c == '1')
        max_count = count


        # 010101
        count = 0
        for i, c in enumerate(s):
            count += (i&1 and c == '1' or i%2 == 0 and c == '0')
        return min(count, max_count)

