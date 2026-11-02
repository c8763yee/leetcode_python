class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if num == []:
            return "0"
            
        stack = [num[0]]
        
        for i in range(1, len(num)):
            prev = num[i-1]
            curr = num[i]
            
            while stack and stack[-1] > curr and k:
                stack.pop()
                k -= 1
            
            stack.append(curr)
        
        while k:
            stack.pop()
            k -= 1
               
        return res if (res:= "".join(stack).lstrip("0")) != "" else "0"