class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        c = Counter(s)
        d = defaultdict(list)
        for k, v in c.items():
            d[v].append(k)


        k, v = max(d.items(), key=lambda pair: (len(pair[1]), pair[0]))
        return "".join(v)