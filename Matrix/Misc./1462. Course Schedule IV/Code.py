class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Store all the direct relationships in a hashmap. Crs ---> pre-req. 
        crs_to_preq_direct = defaultdict(list)

        for preq, crs in prerequisites:
            crs_to_preq_direct[crs].append(preq)
        
        # Now we hv indentified all the direct relationships but indirect still remain.

        # We create a new Hashmap which will store all the relationships of a crs(both D and ID) in a set. We recursively call the dfs function to fill the hashmap for each course.
        def dfs(crs):
            # If the crs is not yet visited we create a set, else return all the preq.
            if crs not in preq_map_indirect:
                preq_map_indirect[crs] = set()

                # For each (Direct) preq of a course filled in first iteration, we recursively fill all the preq in the set.
                for preq in crs_to_preq_direct[crs]:
                    preq_map_indirect[crs] |= dfs(preq)

                # Also adding same crs as its preq of itself   
                preq_map_indirect[crs].add(crs)

            # Returning all the preq of the crs which are also utilized in adding to the sets recursively
            return preq_map_indirect[crs]

        # Map with indirect relationships
        preq_map_indirect = {}
        for crs in range(numCourses):
            dfs(crs)


        res = []
        for preq,crs in queries:
            # Boolean
            res.append(preq in preq_map_indirect[crs])
        
        return res





# O(n^2)      >>>>>>>>>>>>> Worst case where whole graph is fully connected, so each node is preq of all the other nodes
# O(n^2)
