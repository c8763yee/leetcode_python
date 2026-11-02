class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """

        # Intuition:
        since sum of nums is equals to sum of 0 to n and minus the missing number
        we can first calculate the sum of 0 to n and minus the sum of `nums` to get the missing number
        # Complexity:
        Time: O(n), since we need to iterate through the list to calculate the sum
        Space: O(1), since we only use constant space to store the sum of 0 to n
        Args:
            nums (List[int]): _description_

        Returns:
            int: _description_
        """
        n = len(nums)
        size = n * (n + 1) // 2
        return size - sum(nums)

