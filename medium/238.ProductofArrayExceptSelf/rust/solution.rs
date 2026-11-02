impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let size: usize = nums.len();
        let mut dp: Vec<i32> = vec![1;size];
        for i in 1..size{
            dp[i] = dp[i-1] * nums[i-1];
        }
        let mut right: i32 = 1;
        for i in (0..size).rev(){
            dp[i] *= right;
            right *= nums[i];
        }
        dp
    }
}