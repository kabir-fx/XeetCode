class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def baxk(pw, cur_sum):
            if cur_sum == n:
                return True
            if cur_sum > n or 3**pw > n:
                return False
            
            # Include
            if baxk(pw +1, cur_sum + 3**pw):
                return True
            
            # Exclude
            return baxk(pw+1, cur_sum)
        
        return baxk(0, 0)



# O(2^log3(n))
# O(1)
