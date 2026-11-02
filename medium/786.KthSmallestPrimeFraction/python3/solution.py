class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        newarr = [
            (
                float('inf'), 0, 0
            )
            for _ in range((n*(n-1))//2)
        ]
        idx = 0
        for i in range(n):
            for j in range(i+1, n):
                newarr[idx] = (arr[i]/arr[j],arr[i],arr[j])
                idx += 1

        newarr.sort(key=lambda pair: pair[0])
        return newarr[min(k, (n*(n-1))//2)-1][1:]