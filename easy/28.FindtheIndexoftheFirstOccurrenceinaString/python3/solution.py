class Solution:
    def create_table(self, needle, size):
        if size <= 1:
            self.next_table = [-1]
            return
        self.next_table = [-1 for _ in range(size)]
        idx, val = 1, 0
        self.next_table[1] = 0
        while idx <size-1 :
            if val == -1 or needle[idx] == needle[val]:
                idx += 1
                val += 1
                self.next_table[idx] = val
                continue
            val = self.next_table[val]

    def strStr(self, haystack: str, needle: str) -> int:
        len_hay = len(haystack)
        len_nee = len(needle)
        if len_hay < len_nee:
            return -1

        self.create_table(needle, len_nee)
        h, n = 0, 0
        while h <len_hay and n < len_nee:
            if n == -1 or haystack[h] == needle[n]:
                h += 1
                n += 1
                continue
            n = self.next_table[n]
        return (h-n) if n==len_nee else -1