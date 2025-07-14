class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Intuition - First create an adjancy list to collect all the neighbours of all the nodes. We then traverse thru all the nodes with this as our exist condition -
        
            1) If we detect a cycle in the graph
            2) If the all the nodes are not connected
        
        To tackle the False +ve condition of getting the same nb (since the graph is undirected) we will introduce a new paramter = prev that will store the previous value from whose nb this node was picked up.

        To check whether the graph is connected we will compare the len(visitSet) == n, if this is true then the grap is connected
        """

        # Creating an adjancy list
        adj = { i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visitSet = set()
        
        def dfs(i, prev):            
            visitSet.add(i)

            # Traverse all the nb
            for n in adj[i]:
                if n == prev: continue
                if n != prev and n in visitSet: return False

                if not dfs(n, i): return False
            
            return True
            
        return dfs(0, -1) and len(visitSet) == n 



# O(n+e)
# O(n+e)
