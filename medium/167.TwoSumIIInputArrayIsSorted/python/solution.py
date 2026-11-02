class Solution(object):
    def twoSum(self, numbers, target):
        d = {}  # number:index
        for i, n in enumerate(numbers):

            diff = target - n
            if diff in d:
                return [d[diff] + 1, i + 1]
            d[n] = i

        return
