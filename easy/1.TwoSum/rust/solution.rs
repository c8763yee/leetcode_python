use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = HashMap::new();
        for (i, &e) in nums.iter().enumerate(){
            match map.get(&(target - e)) {
                None =>{map.insert(e, i);},
                Some(&index) => {
                    return vec![i as i32, index as i32];
                }
            }   
        }
        vec![]
    }
}