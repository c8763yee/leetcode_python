/*
 * @lc app=leetcode id=342 lang=c
 *
 * [342] Power of Four
 *
 * https://leetcode.com/problems/power-of-four/description/
 *
 * algorithms
 * Easy (49.32%)
 * Likes:    4040
 * Dislikes: 402
 * Total Accepted:    793.6K
 * Total Submissions: 1.6M
 * Testcase Example:  '16'
 *
 * Given an integer n, return true if it is a power of four. Otherwise, return
 * false.
 * 
 * An integer n is a power of four, if there exists an integer x such that n ==
 * 4^x.
 * 
 * 
 * Example 1:
 * Input: n = 16
 * Output: true
 * Example 2:
 * Input: n = 5
 * Output: false
 * Example 3:
 * Input: n = 1
 * Output: true
 * 
 * 
 * Constraints:
 * 
 * 
 * -2^31 <= n <= 2^31 - 1
 * 
 * 
 * 
 * Follow up: Could you solve it without loops/recursion?
 */

// @lc code=start
bool isPowerOfFour(int n)
{
	if (n <= 0) {
		return false;
	}

	return (n & (n - 1)) == 0 && (n & 0xAAAAAAAA) == 0;
}
// @lc code=end
