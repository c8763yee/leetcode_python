impl Solution {
    pub fn count_commas(n: i64) -> i64 {
        let mut threshold: i64 = 1000;
        let mut count: i64 = 0;
        while n >= threshold{
            count += (n-threshold+1);
            threshold *= 1000;
        }
        count
    }
}