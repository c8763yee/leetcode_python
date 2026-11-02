class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        def _inner(s: list[str], i: int = 0):
            if i==n:
                result.append("".join(s))
                return

            for c in "abc":
                if s and c == s[-1]:
                    continue

                s.append(c)
                _inner(s, i+1)
                s.pop()


        _inner([])
        if len(result)<k:
            return ""
        
        return result[k-1]
                


        