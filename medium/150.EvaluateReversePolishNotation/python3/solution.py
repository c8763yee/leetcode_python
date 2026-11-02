class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": lambda a, b: int(a/b)
        }
        stack = []
        for token in tokens:
            if token not in op: # token is int
                stack.append(int(token))
                continue

            # token is one of operator, so check if stack is not empty and eval with top and current token
            if stack != []: 
                right_operand = stack.pop()
                left_operand = stack.pop()
                stack.append(op[token](left_operand, right_operand))

        return stack[0]