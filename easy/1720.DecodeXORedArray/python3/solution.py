class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        a = []
        for i in range(len(encoded)+1):
            if i == 0:
                a.append(first)
                continue
            a.append(encoded[i-1]^a[i-1])
        return a