class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def compare(n):
            if n == 0:
                return mapping[0]

            after = 0
            factor = 1
            while n:
                after += mapping[n % 10] * factor
                n //= 10
                factor *= 10
                
            return after

        return sorted(nums, key=compare)
