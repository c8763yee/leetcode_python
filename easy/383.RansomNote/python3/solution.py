from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """this problem can be reduced to a problem of check if ransomNote is a subset of magazine

        Args:
            ransomNote (str): _description_
            magazine (str): _description_

        Returns:
            bool: _description_
        """
        return not Counter(ransomNote) - Counter(magazine)