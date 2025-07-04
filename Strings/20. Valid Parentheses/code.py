class Solution:
    def isValid(self, s: str) -> bool:
        # Maintain a stack as it will help in popping/appending the brackets
        # Only append the closing brackets in stack as it will help in performing a match with the top element [-1]; if its a match then pop the element.
        
        hel = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        res = []

        for c in s:                 # O(n)
            # Only append if the element is in the hashmap i.e its an openeing bracket
            if c in hel:
                # appending the closing bracket
                res.append(hel[c])

            # Now we are sure that it's a closing bracket

            # Pop only if the stack is non-empty and the top element matches the current closing bracket [i]
            elif res and res[-1] == c:
                res.pop()
            # else return false if coz we are trying to append a closing bracket in an empty stack
            else:
                return False
        
        # returning true only if stack is empty (handling the case if we just append a single "{")
        return len(res) == 0


# O(n)
# O(n)
