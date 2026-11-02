class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popped_idx = 0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[popped_idx]:
                stack.pop()
                popped_idx +=1
        
        while stack:
            if stack.pop() != popped[popped_idx]:
                return False
            popped_idx += 1

        return True