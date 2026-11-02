use std::cmp::{Ordering, max};
impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        if height.len() <= 1{return 0;}

        let mut left: usize = 0;
        let mut left_max: i32 = height[left];
        let mut right: usize = height.len()-1;
        let mut right_max: i32 = height[right];
        let mut size: i32 = 0;
        loop{
            if left_max < right_max{
                left += 1;
                left_max = max(left_max, height[left]);
                size += (left_max - height[left]);
            }else{
                right -= 1;
                right_max = max(right_max, height[right]);
                size += (right_max - height[right]);
            }
            if left >= right{break;}
            }
        size
    }
}