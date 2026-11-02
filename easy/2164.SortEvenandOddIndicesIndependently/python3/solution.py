class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        e=[]
        o=[]
        for i in range(len(nums)):
            t = nums[i]
            if(i%2==0):
                e.append(t)
            else:
                o.append(t)
        e.sort()
        o.sort(reverse=True)
        a=0
        b=0
        for i in range(len(nums)):
            if(i%2==0):
                nums[i]=e[a]
                a+=1
            else:
                nums[i]=o[b]
                b+=1
        return(nums)