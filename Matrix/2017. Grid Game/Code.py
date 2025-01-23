class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # Intuition is to utilize that there are only 2 rows in the ques.

        # First robot wants to minimize the sum for second robot, it does so by gathering all the max points to itself.

        # We find the index at which the partion takes place. For each iteration of i, we aim to maximize the separated top and bottom portion and for the same iteration minimize this maximum given by 1 robot.

        COLS = len(grid[0])

        # Create a copy for both rows in separate arrays as a prefix-sum.
        pre_r1, pre_r2 = grid[0][:], grid[1][:]

        # Appending the values for both the rows creating a Prefix-sum 
        for i in range(1, COLS):
            pre_r1[i] += pre_r1[i-1]
            pre_r2[i] += pre_r2[i-1]
        

        # Initializing the res to max value and then minimizing it.
        res = float("inf")

        for i in range(COLS):
            # Top prefix chunk (RIGHT)
            top = pre_r1[-1] - pre_r1[i]

            # Bottom prefix chunk (LEFT)
            bottom = pre_r2[i-1] if i > 0 else 0
            
            # First robot is choosing the max of both the chunks in order to minimize the sum for second robot
            second_robot = max(top, bottom)

            # Second robot picks the min value from all the iterations
            res = min(res, second_robot)

        return res






# O(n)
# O(n)
