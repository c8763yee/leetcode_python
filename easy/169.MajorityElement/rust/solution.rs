impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut new_nums: Vec<i32> = nums;
        new_nums.sort();
        new_nums[new_nums.len()/2]
    }
}