class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''
        for i in range(min(map(len, (strs)))):
            if all(x[i] == strs[0][i] for x in strs) is False:
                return s
            
            s += strs[0][i]
        return s
