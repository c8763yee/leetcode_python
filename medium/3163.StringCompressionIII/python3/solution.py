class Solution:
    def compressedString(self, word: str) -> str:
        count = 0
        prev = ""
        result = ""
        for c in word:
            if c != prev and prev != '' or count == 9:
                result += (str(count) + prev)
                count = 0
            
            count += 1
            prev = c
        else:
            result += (str(count) + c)

        return result
