use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() { return false }

        let mut h1 = HashMap::new();
        let mut h2 = HashMap::new();

        // Zip clubs 2 separate iterators into a tuple (i1, i2) essentially combining their results
        for (c1, c2) in s.chars().zip(t.chars()) {
            // References to the c1 key in h1 and then increments its value
            *h1.entry(c1).or_insert(0) += 1;
            *h2.entry(c2).or_insert(0) += 1;
        }

        h1 == h2
    }
}


// O(n)
// O(n)
