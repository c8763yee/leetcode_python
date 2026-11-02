class Solution:
    def validStrings(self, n: int) -> List[str]:
        dp = ['0', '1']
        for i in range(1, n):
            tmp = []
            for ele in dp:
                for c in '01':
                    if ele[-1] == '1' or c == '1':
                        tmp.append(ele+c)
            dp = tmp
        return dp
