impl Solution {
    pub fn count_servers(grid: Vec<Vec<i32>>) -> i32 {
        let row = grid.len();
        let col = grid[0].len();

        let mut row_cnt = vec![0; row]; 
        let mut col_cnt = vec![0; col]; 

        for r in 0..row {
            for c in 0..col {
                if grid[r][c] == 1 {
                    row_cnt[r] += 1;
                    col_cnt[c] += 1;
                }
            }
        }

        let mut res = 0;

        for r in 0..row {
            for c in 0..col {
                if grid[r][c] == 1 {
                    if (row_cnt[r] > 1) || (col_cnt[c] > 1){
                        res += 1;
                    }
                }
            }
        }

        res
    }
}
