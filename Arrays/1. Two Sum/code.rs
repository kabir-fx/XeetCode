use std::collections::HashMap;
impl Solution {    
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = HashMap::new();

        for (i, n) in nums.iter().enumerate() {
            // .get() expects a reference value as input thus so does Some as well here
            if let Some(&j) = map.get(&(target - n)) {
                return vec![j, i as i32];
            }
            map.insert(*n, i as i32);
        }
        vec![] // Return empty vector if no solution found
    }
}


// O(n)
// O(n)
