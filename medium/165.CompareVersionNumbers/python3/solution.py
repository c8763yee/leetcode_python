class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_lst = list(map(int, version1.split('.')))
        v2_lst = list(map(int, version2.split('.')))
        for i in range(min(len(v1_lst), len(v2_lst))):
            if v1_lst[i] < v2_lst[i]:
                return -1
            elif v1_lst[i] > v2_lst[i]:
                return 1
            
        flag = 1
        lst = None
        if len(v1_lst) == len(v2_lst):
            return 0
        elif len(v1_lst) < len(v2_lst):
            flag = -1
            lst = v2_lst[i+1:]
        else:
            lst = v1_lst[i+1:]

        return flag if any(i != 0 for i in lst) else 0