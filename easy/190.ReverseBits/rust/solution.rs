impl Solution {
    pub fn reverse_bits(x: u32) -> u32 {
        let mut reversed_x: u32 = 0;
        let mut mut_x = x;
        let mut bits = 32;
        while mut_x != 0{
            reversed_x <<= 1;
            reversed_x += (mut_x&1);
            mut_x >>= 1;
            bits -= 1;
        }
        reversed_x <<= bits;
        reversed_x
    }
}