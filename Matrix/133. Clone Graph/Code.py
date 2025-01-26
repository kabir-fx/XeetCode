"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Intuition: WE iterate over each node and its neighbors recursively and keep appending them to the copy node. 
        # For each node we create a copy and append it to a hashmap as a val corresponding to the original node. The function returns the reference of the current copy node so it can be easily appended as a neighbor/returned as the res.
        #  WE then iterate over each of itd neighbors and determine whther its present in the hashmap, if yes it means its visited we then return the val(reference to the copy node) else we create the copy of the node and then append it into the hashmap.

        # Node ---> Copy Node
        hashmap = {}

        def dfs(node):
            if node in hashmap:
                return hashmap[node]
            
            copy = Node(node.val)
            hashmap[node] = copy

            for n in node.neighbors:
                # For each nb of the orginal we create their copy recursively and append to the nb of the current copy node
                copy.neighbors.append(
                    dfs(n)
                )
            
            return copy
        
        return dfs(node) if node else None





# O(V+E)    -----> For the worst case every node and edge is visited once
# O(V)
