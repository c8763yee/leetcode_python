# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            print(mid)
            if isBadVersion(mid):
                if isBadVersion(mid-1) is False:
                    return mid
                right = mid-1
            else:
                if isBadVersion(mid+1):
                    return mid+1
                left = mid+1

        return left
