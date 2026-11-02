use std::collections::HashMap;
impl Solution {
    pub fn num_identical_pairs(nums: Vec<i32>) -> i32 {
        let mut map: HashMap<i32, i32> = HashMap::new();
        let mut total: i32 = 0;
        for key in nums{
            *map.entry(key).or_default() += 1
        }
        // pr/intln!("map: {:?}", map);
        for(h,value) in map{
            total += (value - 1) * value / 2;
        }
        total
    }
}