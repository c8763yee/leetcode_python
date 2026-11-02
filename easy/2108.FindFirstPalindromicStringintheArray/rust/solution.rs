impl Solution {
    pub fn first_palindrome(words: Vec<String>) -> String {
        match words.iter().filter(|word| {
            let rev = word.chars().rev().collect::<String>();
            **word==rev}
        ).next(){
            None => {"".to_string()},
            Some(palindromic_string) => {
                palindromic_string.to_string()
            }
        }
    }
}