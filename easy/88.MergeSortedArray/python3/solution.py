class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #if nums2 is empty then just exit function
        if n==0:
            return
        #if nums1 is empty then move everything from nums2 to num1 and exit
        if m==0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        
        k = m+n-1
        m-=1
        n-=1
        
        while(m>=0 and n>=0):
            if nums1[m]> nums2[n]:
                nums1[k] = nums1[m]
                m-=1
            else:
                nums1[k] = nums2[n]
                n-=1
            k-=1
        while n>=0:
            nums1[k] = nums2[n]
            n-=1
            k-=1
                
        