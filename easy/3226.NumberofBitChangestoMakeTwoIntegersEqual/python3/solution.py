class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if k > n:
            return -1
        count = 0

        while n:
            if n%2 == 0 and k%2:
                return -1

            if n%2 and k%2==0:
                count += 1

            n //= 2
            k //= 2

        return count



        #1101
        #1110