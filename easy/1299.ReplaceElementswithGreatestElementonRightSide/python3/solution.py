class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        max_ = arr[l-1]
        arr[l-1] = -1
        for i in range(l-2, -1, -1):
            t = arr[i]
            arr[i] = max_ 
            if t> max_:
                max_ = t
        return arr