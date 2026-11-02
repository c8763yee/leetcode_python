impl Solution {
    pub fn is_power_of_two(n: i32) -> bool {
        match n.checked_sub(1)
        .and_then(|x| x.checked_add(1))
        .or_else(||None){
            None => {false},
            Some(x) =>{
                x&(x-1) == 0 && x != 0
            }
        }
    }
}