class Solution:
    def addToArrayForm(self, num: list[int], k: int, idx=-1) -> list[int]:
        leng = len(num)
        while k != 0:
            if ~idx >= leng:
                num.insert(0, k%10)
                leng +=1
            else:
                num[idx] += k%10             
            k //=10
            idx -=1
        
        for idx in range(-1, -1-leng, -1):
            if num[idx] >= 10:
                num[idx] -=10
                if idx == -leng:
                    num.insert(0, 1)
                else:
                    num[idx-1] += 1
        return num


