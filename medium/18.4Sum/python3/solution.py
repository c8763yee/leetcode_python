class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        lst = set()
        def two_sum(target, start):
            d = {}
            for idx in range(start, n):
                if nums[idx] in d:
                    return idx, d[nums[idx]], True
                d[target-nums[idx]] = idx
            return 0, 0, False
        for i in range(n - 3):
            for j in range(i+1, n-2):
                a = j + 1
                b = n - 1
                while a<b:
                    cur = nums[a]+nums[b]+nums[i]+nums[j]
                    if cur == target:
                        lst.add((nums[a],nums[b],nums[i],nums[j]))
                        a += 1
                        b -= 1
                    elif cur < target:
                        a += 1
                    else:
                        b -= 1
        return lst

        return lst
                