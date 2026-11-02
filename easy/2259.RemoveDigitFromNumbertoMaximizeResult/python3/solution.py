class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        occur = []
        for i, s in enumerate(number):
            if s == digit:
                occur.append(i)
        
        maximum = 0 
        for i in occur: #O(N)
            new_str = number[0:i] + number[i+1:] #O(N)
            maximum = max(maximum, int(new_str))
                
        return str(maximum)