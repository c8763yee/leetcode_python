impl Solution {
    pub fn my_pow(x: f64, n: i32) -> f64 {
        let mut x = x;
        let mut n = n;
        if x == 1.0 || n == 0 {
            return 1.0;
        }
        if x == 0.0{
            return 0.0
        }
        if n == 1{
            return x;
        }
        if n < 0{
            x = 1.0/x;
        }
        println!("n={n}\nx={x}\n\n");
        Self::my_pow(x*x, (n/2).abs()) * if n&1==1 {x} else {1.0}
    }
}