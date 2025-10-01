class Solution:
    def numWaterBottles(self, nb: int, ne: int) -> int:
        """
        Intuition: Our goal is to ensure that after we are done drinking - we are left with < echange bottles (including the bottles we get after drinking the exchange bottles).

        To facilitate this we cal. bottles left after each round before giving bottles to the exchange and add them up to the bottles we will recieve after drinking.
        """
        
        res = nb
        cur = nb

        while cur >= ne:
            res += cur // ne
            
            cur = cur - ((cur // ne) * ne) + (cur // ne)
        
        return res


# O(log(num of bottles))                | Since we are dividing the bottles at each step
# O(1)
