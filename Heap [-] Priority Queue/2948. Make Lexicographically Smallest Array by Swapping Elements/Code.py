class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # Intuition is to first indentify the groups into which we can devide the array (of abs val less than limit) and then indivdually sort thier elements.
        # For this we first need to determine - How will we map in the resultant array that each element belongs to which group and which DS to use for groups.

        # WE use a list comprising of queue(s) as they can be used to pop the smallest element in O(1) time from AFTER SORTING THE ARRAY
        group = []

        # Hashmap to map each element to their respective index of the queue in group
        map = {}


        # We first sort the array(To easily determine groups by subtracting consecutive elements) and then iterate over each element to populate the group and Hashmap
        for n in sorted(nums):
            # If the group is empty or abs value exceeds the limit we intialize a new queue within the group.
            if not group or abs(n - group[-1][-1]) > limit:
                group.append(deque())
            
            # We then start populating the queue(latest). We dont require the index of the queue present in prev index as once we append a new group no element will hv the abs value low enough to pass the limit as all elements in this array are sorted
            group[-1].append(n)

            # Map the index of the latest appended queue to the current element for the aforementioned reason
            map[n] = len(group) - 1    



        res = []

        for n in nums:
            # Fetching the index of the queue containing the element thru Hashmap
            index = map[n]

            # Popping the elemeent from the queue which will always result in the smallest element of that queue
            res.append(
                group[index].popleft()
            )
        
        return res





# O(n)
# O(n)
