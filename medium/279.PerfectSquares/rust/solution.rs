fn is_pow(n: i32) -> bool {
    ((n as f64).sqrt() as i32).pow(2) == n
}
impl Solution {
    pub fn num_squares(n: i32) -> i32 {
        let mut n = n;
        while n%4 == 0{
            n /= 4;
        }
        if n%8 == 7{
            return 4;
        }
        if is_pow(n){
            return 1;
        }
        for i in (1..=(n as f64).sqrt() as i32) {
            let remain = n - i * i;
            if is_pow(remain){
                return 2;
            }
        }
        3
    }
}