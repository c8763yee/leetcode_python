def get_diff(n):
    count = [0 for _ in range(10)]
    while(n):
        count[n%10] += 1
        n //= 10

    for i in range(9,-1,-1):
        while count[i]:
            n = n*10+i
            count[i]-=1
    return n
    
def sort_diff(n):
    return n - get_diff(n)
    

class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        nums.sort(key=sort_diff)
        for i in range(k):
            nums[i] = get_diff(nums[i])
        return sum(nums)