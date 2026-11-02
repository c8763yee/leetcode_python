class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return len(pattern) == len((st:= s.split())) and len(set(zip(pattern, st))) == len(set(pattern)) == len(set(st)) 
            