class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        avail = numBottles
        empty = 0
        count = 0
        while avail:
            # drink
            count += avail
            empty += avail
            avail = 0

            # exchange
            avail += empty // numExchange
            empty %= numExchange
            


        return count