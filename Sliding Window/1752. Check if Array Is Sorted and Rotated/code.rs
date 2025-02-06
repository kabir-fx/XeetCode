impl Solution {
    pub fn check(nums: Vec<i32>) -> bool {
        let mut cnt = 1;
        let n = nums.len();

        if n == cnt {return true}

        for i in 1..(2*n){
            if nums[(i-1) % n] <= nums[i%n] {
                cnt += 1;

                if cnt == n {return true}
            } else {
                cnt = 1
            }
        }

        false
    }
}



// O(n)
// O(1)
