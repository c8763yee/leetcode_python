class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0 for _ in code]

        code_copy = code.copy()
        for i, e in enumerate(code):
            num = 0
            for diff in range(1, abs(k)+1):
                index = (i + (diff if k > 0 else -diff))%len(code)
                num += code[index]
            code_copy[i] = num
        return code_copy
