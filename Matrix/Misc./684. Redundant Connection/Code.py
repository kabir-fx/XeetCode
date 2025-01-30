class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # First find the cycle in the graph and append all the nodes in the cycle to a hashset. Iterate from the end of "edges" and return the first pair in the hashset.
        n = len(edges)

        # Store all the neighbors for all edges. (n+1) coz all the nodes are 1-indexed. So even though the 0 index element is useless we can access 1 node given thru input at 1 index of our struc.
        adj = [[] for _ in range(n+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Mark all the nodes as NOT visited, yet
        visited = [False] * (n+1)
        # Node marking the start of the cycle
        start_cycle = -1
        cycle = set()

        # dfs runs until it keeps returning True. Aim is to fill the cycle set with all the nodes present in the cycle. 
        def dfs(node, par):
            nonlocal start_cycle

            # Start returning True once the nodes start repeating
            if visited[node]:
                start_cycle = node
                return True
            
            # Mark current node as visited
            visited[node] = True

            # For each node that is connected we recursively run dfs. For a cycle it will recursively keep returning us Truem thus allowing to easily fill out the cycle set.
            for nb in adj[node]:
                # Skip the Parent
                if nb == par:
                    continue

                # If the func. keeps returning True
                if dfs(nb, node):
                    # Means cycle has already been started so appending the current node to cycle set.
                    if start_cycle != -1:
                        cycle.add(node)

                    # All the nodes have been added to the cycle, setting the start_cycle as -1 to return False in the next iteration and exit out the dfs.
                    if start_cycle == node:
                        start_cycle = -1

                    return True

            # Return false to break out the dfs
            return False


        # Since root doesnt hv parent so giving -1 as it will never be present
        dfs(1, -1)

        # First pair to appear in set gets returned
        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]





# O(n)
# O(n)
