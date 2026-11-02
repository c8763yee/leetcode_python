class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        def drunk(n, e, ex):
            drunked = n
            if n+e < ex:
                return drunked
            
            e += n
            n = 0
            while e >= ex:
                e -= ex
                n += 1
                ex += 1
            
            return drunked + drunk(n, e, ex)
        
        return drunk(numBottles, 0, numExchange)