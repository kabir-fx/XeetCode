class TimeMap:
    # Intuition: Use a hashmap to store a key-value like data structure. For values we need to  store them in order to retrieve a closest timestamp to the given query that is we need to select the maximum value of the given key. 
    def __init__(self):
        self.store = {}        # key: list of values ~ [value, timestamp] 

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Use a list to store all values
        if key not in self.store:
            self.store[key] = []

        # Append the value against the corresponsing key in the list as their can be multiple values of same key
        self.store[key].append([timestamp, value])
    

    # O(1)

    def get(self, key: str, timestamp: int) -> str:
        # Get all the values for a corresponding key else a []
        values = self.store.get(key, [])

        l,r = 0, len(values) -1

        res = ""
        while l <= r:
            m = (l+r) // 2

            if values[m][0] <= timestamp:
                # We are always maximizing our timestamp in the values to get closest to the one asked in the query
                res = values[m][1]

                l = m + 1
            else:
                r = m - 1

        return res        


    
    # O(logn)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
