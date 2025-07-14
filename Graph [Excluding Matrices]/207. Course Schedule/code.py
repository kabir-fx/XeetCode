class Solution:
    def canFinish(self, n: int, preq: List[List[int]]) -> bool:
        """
        Intuition - Use a adj list to store all the nb, then iterate thur all the nb and use a visitSet to determine a cycle. If a cyclic return True.

        We maintain a running set which contains all the courses we hv traversed in the current traversal.

        After we are done traversing and hv observed the current path to be acyclic we then remove the current course (index) from both set and the adj list, in order to reduce time complexity.

        This Graph can be disconnected - that's why we run dfs on each and every index.
        """
        if len(preq) <= 1: return True

        # Creating an ADJ list
        adj = { i:[] for i in range(n)}
        for n1,n2 in preq:
            adj[n1].append(n2)

        visitSet = set()

        def dfs(i):
            visitSet.add(i)

            # Traverse thru all the nb
            for n in adj[i]:
                # If the n is repeating in the current iteration of visitSet - graph is cyclic
                if n in visitSet: return False

                if not dfs(n): return False
            
            # Improving the compexity by removing already verified nodes from both set and map
            visitSet.remove(i)
            adj[i] = []

            return True

        for crs in range(n):
            if not dfs(crs): return False
        
        return True


# O(n.(n+e))
# O(n+e)
