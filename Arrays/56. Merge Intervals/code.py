class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Intuition: we need to sort the intervals array which will help in indentifying the merging pairs.
        # Sorting will ensure that whenever we see a pair's start value is less than the last appended pair's end value - its a merging pair

        # Function to sort the 2D arr based on first element. i is the intervals array and i[0] indicates the key is the first pair.
        intervals.sort(key = lambda i : i[0])       # O(n.logn)
        output = [intervals[0]]

        for start, end in intervals[1:]:            # O(n)
            lastEnd = output[-1][1]

            # IF the last appended value is larger than the current first value.
            if lastEnd >= start:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])

        return output


# O(nlogn)
# O(n)
