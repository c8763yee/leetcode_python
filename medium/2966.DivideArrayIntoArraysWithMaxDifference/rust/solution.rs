use std::cmp::Ordering;

impl Solution {
    pub fn divide_array(nums: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        let mut alt_nums: Vec<i32> = nums.clone();
        alt_nums.sort();
        let nums: Vec<i32> = alt_nums;

        let result: Vec<Vec<i32>> = nums.chunks_exact(3)
            .map(|chunk| {
                let first_element = chunk[0];
                chunk.iter()
                    .map(|&num| (num, (num - first_element).cmp(&k)))
                    .take_while(|&(_, ordering)| ordering != Ordering::Greater)
                    .map(|(num, _)| num)
                    .collect::<Vec<i32>>()
            })
            .collect();

        if result.iter().all(|subarray| subarray.len() == 3) {
            result
        } else {
            vec![]
        }
    }
}