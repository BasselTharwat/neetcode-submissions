# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    # This hashmap map the old reference of the node to the new reference
    # Also used to prevent loops
    def __init__(self):
        self.oldToNew = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # If the graph has no nodes
        if node is None:
            return node

        # If the node's copy is found in the hashmap, return the copy
        if node in self.oldToNew:
            return self.oldToNew[node]

        # Else, create a copy of the node and add it to the hashmap
        newNode = Node(node.val)
        self.oldToNew[node] = newNode

        # recursively do the same for all the neighbors
        for neighbor in node.neighbors:
            # create a copy of the node and append it's neighbors to the copy
            neighborNode = self.cloneGraph(neighbor)
            newNode.neighbors.append(neighborNode)

        return newNode
            
        
        
        
        

        
        return node
        