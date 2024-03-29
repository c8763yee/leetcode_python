#
# @lc app=leetcode id=2966 lang=python3
#
# [2966] Divide Array Into Arrays With Max Difference
#
# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/
#
# algorithms
# Medium (56.91%)
# Likes:    187
# Dislikes: 45
# Total Accepted:    37.4K
# Total Submissions: 58.5K
# Testcase Example:  '[1,3,4,8,7,9,3,5,1]\n2'
#
# You are given an integer array nums of size n and a positive integer k.
#
# Divide the array into one or more arrays of size 3 satisfying the following
# conditions:
#
#
# Each element of nums should be in exactly one array.
# The difference between any two elements in one array is less than or equal to
# k.
#
#
# Return a 2D array containing all the arrays. If it is impossible to satisfy
# the conditions, return an empty array. And if there are multiple answers,
# return any of them.
#
#
# Example 1:
#
#
# Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
# Output: [[1,1,3],[3,4,5],[7,8,9]]
# Explanation: We can divide the array into the following arrays: [1,1,3],
# [3,4,5] and [7,8,9].
# The difference between any two elements in each array is less than or equal
# to 2.
# Note that the order of elements is not important.
#
#
# Example 2:
#
#
# Input: nums = [1,3,3,2,7,3], k = 3
# Output: []
# Explanation: It is not possible to divide the array satisfying all the
# conditions.
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 10^5
# n is a multiple of 3.
# 1 <= nums[i] <= 10^5
# 1 <= k <= 10^5
#
#
#

# @lc code=start
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(0, n, 3):
            if i + 2 < n and nums[i + 2] - nums[i] <= k:
                ans.append([nums[i], nums[i + 1], nums[i + 2]])
            else:
                return []
        return ans
# @lc code=end
