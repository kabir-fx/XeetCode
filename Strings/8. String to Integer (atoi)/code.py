class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Intuition: The problem seems easy in theory but sucks out your life once you start acutally implementing it. Our aim is to return the cur res as soon as we hit any non store character. Otherwise this problem follows implementing the given rules carefully
        """

        INT_MAX = 2147483647
        INT_MIN = -2147483648

        store = ["0","1","2","3","4","5","6","7","8","9"]
        
        flag = False
        flag2 = False
        
        res = ""
        
        for c in s:                                 # O(n)
            if c == ' ' and not flag2: continue
            if c not in store:
                if not flag2:
                    if c == '-':
                        flag = True
                        flag2 = True
                    elif c == '+':
                        flag2 = True
                    else:
                        break
                elif flag2: break
            else:
                flag2 = True

                res += c
        
        if res == "": return 0

        res_int = int(res)
        if res_int > INT_MAX:
            return INT_MIN if flag else INT_MAX
        else:
            return -res_int if flag else res_int


# O(n)
# O(n)
