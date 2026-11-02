class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        r = ['' for _ in indices]
        for idx in indices:
            r[indices[idx]] = s[idx]
        return ''.join(r)