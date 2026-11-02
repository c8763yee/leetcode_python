class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        nums.sort(key=lambda x: -x)
        while nums:
            alice = nums.pop()
            bob = nums.pop()
            
            arr.append(bob)
            arr.append(alice)
            
        return arr
            
            