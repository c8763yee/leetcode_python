class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        hm = dict()
        for i, e in enumerate(score):
            hm[e] = i

        newscore = sorted(score, reverse=True)
        newarr = [0 for _ in score]
        for i, e in enumerate(newscore, 1):
            if i == 1:
                newarr[hm[e]] = "Gold Medal"
            elif i == 2:
                newarr[hm[e]] = "Silver Medal"
            elif i == 3:
                newarr[hm[e]] = "Bronze Medal"
            else:
                newarr[hm[e]] = str(i)
        return newarr

