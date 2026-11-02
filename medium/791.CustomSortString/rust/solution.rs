use std::collections::HashMap;

impl Solution {
    pub fn custom_sort_string(order: String, mut s: String) -> String {
        let mut counter = HashMap::new();
        for (i, c) in order.chars().enumerate() {
            counter.insert(c, i);
        }
        let mut chars: Vec<char> = s.chars().collect();
        chars.sort_by(|a, b| {
            let a_val = *counter.get(a).unwrap_or(&usize::MAX);
            let b_val = *counter.get(b).unwrap_or(&usize::MAX);
            a_val.cmp(&b_val)
        });
        chars.into_iter().collect()
    }
}