impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return false;
        }
        
        let mut alt_x: i32 = 0;
        let mut remaining_x = x;

        while remaining_x != 0 {
            match alt_x.checked_mul(10).and_then(|mul_x| mul_x.checked_add(remaining_x % 10)) {
                Some(new_alt_x) => {
                    alt_x = new_alt_x;
                    remaining_x /= 10;
                }
                None => {
                    return false; // Exit the function early if overflow occurs
                }
            };
        }

        alt_x == x
    }
}
