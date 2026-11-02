class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        ptr='a'
        for c in word:
            # move ptr to c
            if c != ptr:
                diff = ord(c) - ord(ptr)
                ptr = c
                time += min(abs(diff-26)%26, diff%26)
            # type c
            time += 1
        return time
