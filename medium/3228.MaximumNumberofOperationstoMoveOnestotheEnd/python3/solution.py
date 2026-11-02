class Solution:
    def maxOperations(self, s: str) -> int:
        flag = 2
        one_count = 0
        ope = 0


        prev = ''
        for i, e in enumerate(s):
            # print(e, one_count, ope, flag, sep=', ')
            if prev and e != prev:
                flag -= 1
                if flag == 0:
                    flag = 2                    
                    ope += one_count

            one_count += int(e=='1') 
            prev = e
        
        # print(flag, one_count, ope)
        if flag == 1 and prev == '0':
            ope += one_count
        return ope