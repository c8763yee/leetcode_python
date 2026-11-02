class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        size = len(senate)
        Radiant = deque()
        dire = deque()
        for i, e in enumerate(senate):
            if e == 'R':
                Radiant.append(i)
            else:
                dire.append(i)

        while Radiant and dire:
            r = Radiant.popleft()
            d = dire.popleft()
            if r < d:
                Radiant.append(r+size)
            else:
                dire.append(d+size)
        return 'Radiant' if Radiant else 'Dire'
