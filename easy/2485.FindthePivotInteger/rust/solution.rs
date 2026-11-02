/*
class Solution:
    def pivotInteger(self, n: int) -> int:
        right_sum = (n+1)*n//2
        left_sum = 0
        for left in range(1, n+1):
            left_sum += left
            if left_sum == right_sum:
                return left
            right_sum -= left

        return -1
        
*/
impl Solution {
    pub fn pivot_integer(n: i32) -> i32 {
        let mut right_sum: i32 = (n+1)*n/2;
        let mut left_sum: i32 = 0;
        for left in 1..=n{
            left_sum += left;
            if left_sum == right_sum{return left;}
            right_sum -= left;
        }
        -1
    }
}