mapping = [None, None, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        def dfs(idx, size, words):
            if idx >= size:
                if idx == size and words!="":
                    result.append(words)
                return 

            for c in mapping[int(digits[idx])]:
                dfs(idx+1, size, words+c)

        dfs(0, len(digits), "")
        return result


            