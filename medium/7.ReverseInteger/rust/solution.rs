impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut new_x: i32 = 0;
        let sign: i32 = if x >= 0 {1} else {-1};
        let mut x: i32 = x.abs();
        while x != 0 {
            match new_x.checked_mul(10).and_then(|muled_x| muled_x.checked_add(x%10)){
                None => {return 0;},
                Some(checked_x) => {
                    new_x = checked_x;
                    x /= 10;
                }
            }
        }
        return new_x * sign;
    }
}