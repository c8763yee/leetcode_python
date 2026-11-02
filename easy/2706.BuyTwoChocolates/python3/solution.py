class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        """
        T.C: O(n log(n)) // sorting
        S.C: O(1)
        """
        # sort list to asec
        a = b = 101
        for i in prices:
            if i <= a:
                b = a
                a = i
            elif i <= b:
                b = i


        total = a+b
        if total > money:
            return money

        return money-total