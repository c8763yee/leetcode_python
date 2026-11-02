/*
class Solution:
    def rob(self, nums: List[int]) -> int:
       next_val = b = 0
        for i in nums:
           next_val, b = max(b+i,next_val),next_val

        returnnext_val

*/
use std::cmp::{max,min};
impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let mut next_val: i32 = 0;
        let mut prev_val: i32 = 0;
        for curr_num in nums{
            let temp = next_val;
            next_val = max(curr_num+prev_val, next_val);
            prev_val = temp;
        }
       next_val
    }
}