class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def find(first, second, score):
            stack = []
            total_score = 0
            for c in s:
                if stack and stack[-1] == first and c == second:
                    stack.pop()
                    total_score += score
                else:
                    stack.append(c)
            return ''.join(stack), total_score
        

        if x > y:
            s, score1 = find('a', 'b', x)
            _, score2 = find('b', 'a', y)
        else:
            s, score1 = find('b', 'a', y)
            _, score2 = find('a', 'b', x)

        return score1 + score2 