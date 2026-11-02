class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0 for _ in range(num_people)]
        idx = 0
        while candies >idx:
            ans[idx%num_people]+= idx+1
            candies -=(idx+1)
            idx+=1
        ans[idx%num_people]+= candies
        return ans