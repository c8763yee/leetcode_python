impl Solution {
    pub fn minimum_length(s: String) -> i32 {
        /*
        class Solution:
            def minimumLength(self, s: str) -> int:
                size = len(s)
                left = 0
                right = size - 1

                while left < right:
                    if s[left] != s[right]:
                        return right - left + 1
                    
                    prefix_first = s[left]
                    while left < right and s[left] == prefix_first:
                        left += 1
                    while left < right and s[right] == prefix_first:
                        right -= 1
                
                return int(left == right)
        */
        let s_chars: Vec<char> = s.chars().collect();

        let size: usize = s.len();
        let mut left: usize = 0;
        let mut right: usize = size - 1;
        while left < right{
            if s_chars[left] != s_chars[right]{
                return (right - left + 1) as i32;
            }
            let prefix_first: char = s_chars[left];
            loop{
                left += 1;
                if s_chars[left] != prefix_first{break}
                else if left == right{return 0;}
            }
            loop{
                right -= 1;
                if s_chars[right] != prefix_first{break}
                else if left == right{return 0;}
            }
        }
        if left == right {1} else {0}
    }
}