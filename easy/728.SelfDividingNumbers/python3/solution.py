class Solution:
    def isSelfDividing(self, num: int):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in num_str:
            if num % int(i):
                return False 
            
            
        return True
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return list(filter(self.isSelfDividing,range(left, right+1)))