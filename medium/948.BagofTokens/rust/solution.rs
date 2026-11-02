use std::cmp::max;
impl Solution {
    pub fn bag_of_tokens_score(tokens: Vec<i32>, power: i32) -> i32 {
        if tokens.len() == 0{return 0;}
        let mut power = power;
        let mut tokens: Vec<i32> = tokens.clone();
        tokens.sort();
        
        let mut left: usize = 0;
        let mut right: usize = tokens.len() - 1;
        
        let mut score: i32 = 0;
        let mut max_score: i32 = 0;



        while left <= right {
            if power >= tokens[left]{
                power -= tokens[left];
                score += 1;
                left += 1;
                max_score = max(score, max_score);
            }
            else if score > 0{
                power += tokens[right];
                score -= 1;
                right -= 1;
            }
            else{
                break;
            }
        }
        max_score
    }
}