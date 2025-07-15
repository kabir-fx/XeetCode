class Solution:
    def findOrder(self, n: int, preq: List[List[int]]) -> List[int]:
        """
        GRAPH PROBLEM

        INTUITION - we will first an adjancy list to store all the nodes and their corresponding nb. We will then iterate over all the nb to determine whether the graph is cyclic.

        We will use 4 DS to solve this:
            visited = set to determine all the nodes we have visited that dont need to be visited again.
            visiting = set that will be used in the current traversal of nodes to determine whether the graph is cyclic
            adj = adjancy list to store all nodes and corresponding nb
            res = list that will store our path
        
        DS:
            visited = Hashset
            visiting = Hashset
            adj = Hashmap { node: [nb1, nb2, ...., nb]}
            res = List
        
        We hv to use visited otherwise we will end up appending the same node to res multiple times.
        """

        # Populate all nodes and nb
        adj = { i:[] for i in range(n) }
        for crs, pre in preq:
            adj[crs].append(pre)
        
        visited, visiting = set(), set()
        res = []

        def dfs(i) -> bool:
            if i in visiting: return False
            if i in visited: return True

            visiting.add(i)

            for n in adj[i]:
                if not dfs(n): return False

            visiting.remove(i)
            visited.add(i)
            res.append(i)

            return True

        for i in range(n):
            if not dfs(i): return []
        
        return res



# O(e+n)
# O(e+n)
