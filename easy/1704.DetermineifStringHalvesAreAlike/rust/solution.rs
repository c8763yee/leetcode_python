use std::cmp::Ordering;
use std::collections::HashSet;
use std::iter::FromIterator;
impl Solution{
    pub fn halves_are_alike(s: String) -> bool {
        let size: usize = s.len();
        let half = size / 2;
        let VOWEL: String = String::from("aeiouAEIOU");
        let vowel_set: HashSet<char> = VOWEL.chars().collect();
        let mut vowel_count: i32= 0;
        for (left, c) in s.chars().enumerate() {
            if vowel_set.contains(&c){
                vowel_count += if left < half {1} else {-1};
            }
        }
        vowel_count == 0
    }
}