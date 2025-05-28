use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut h = HashMap::new();

        for s in strs {
            let mut cnt = vec![0; 26];
              for c in s.chars() {
                /*
                [as u8] to convert the char into its ascii value
                
                [as usize] that's what the entry of hashmap accepts

                [b'a'] returns the ascii value of char a
                */
                cnt[(c as u8 - b'a') as usize] += 1;
            } 

            /*
            [entry()] accesses the entry of cnt in hashmap

            [or_inset_with()] if no entry is present, it then creates one vector type

            [push()] appends the word, corresponding to the entry
            */
            h.entry(cnt).or_insert_with(Vec::new).push(s);
        }

        /*
        [values()] provides as interator over all the values in hashmap

        [cloned()] clones and converts the &n from values() to n 
        */
        h.values().cloned().collect()
    }
}
