class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for cs, ct in zip(s, t):
            if cs not in s_map and ct not in t_map:
                s_map[cs] = ct
                t_map[ct] = cs
            elif s_map.get(cs) != ct or t_map.get(ct) != cs:
                return False

        return True