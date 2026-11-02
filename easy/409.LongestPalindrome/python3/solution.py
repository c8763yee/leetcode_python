from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        # Intuition:
            count all occurences of each character, then add up all even counts
            if there is any odd count, add 1 to the result.
        # complexity:
            $O(n)$ T.C , because we need to iterate through the string once and count the occurences
            $O(n)$ S.C, because we need to create a hashmap to store the occurences of each character

        Args:
            s (str): _description_

        Returns:
            int: _description_
        """
        total = 0
        is_odd = False
        for v in Counter(s).values():
            if v == 1:
                is_odd = True
            else:
                total += v // 2
                is_odd = is_odd or v % 2 == 1

        return total * 2 + is_odd