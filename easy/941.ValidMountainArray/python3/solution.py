class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n<3: return False
        i=0
        while i+1<n and arr[i+1]>arr[i]:
            i+=1
        
        if i==0 or i+1 == n:
            return False
        
        while i+1<n and arr[i] > arr[i+1]:
            i+=1
        return i+1==n