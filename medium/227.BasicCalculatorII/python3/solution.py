class Solution:
    def calculate(self, s: str) -> int:
        nums = [c for c in re.findall("([0-9]*|[\+\-\*/])", s) if c]
        stack = []
        for c in nums:
            if c.isdigit() is False:
                stack.append(c)
                continue
            
            num = int(c)
            if stack and stack[-1] in "*/":
                op = stack.pop()
                stack[-1] = (stack[-1] // num if op == "/" else stack[-1] * num)
            else:
                stack.append(num)
    
        for i in range(0, len(stack)-2, 2):
            stack[i+2] = stack[i] + (stack[i+2] if stack[i+1] == '+' else -stack[i+2])


        return stack[-1]
