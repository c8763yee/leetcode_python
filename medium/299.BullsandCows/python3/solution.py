class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        maps = Counter(secret)
        A = B = 0
        remain = []
        for i, (s, g) in enumerate(zip(secret, guess)):
            if s == g:
                A += 1
                maps[s] -= 1
            else:
                remain.append(g)

        for g in remain:
            if maps.get(g, 0) > 0:
                B += 1
                maps[g] -= 1
        return f'{A}A{B}B'

