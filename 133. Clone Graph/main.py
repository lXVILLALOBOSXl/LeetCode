# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}
        return self.cloneGraphHelper(node, visited)
    
    def cloneGraphHelper(self, node: 'Node', visited: dict[int, 'Node']) -> 'Node':
        if node.val in visited:
            return visited[node.val]
        new_node = Node(node.val)
        visited[node.val] = new_node
        for neighbor in node.neighbors:
            new_node.neighbors.append(self.cloneGraphHelper(neighbor, visited))
        return new_node
        

# Test cases
s = Solution()
Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node1.neighbors = [Node2, Node4]
Node2.neighbors = [Node1, Node3]
Node3.neighbors = [Node2, Node4]
Node4.neighbors = [Node1, Node3]
result = s.cloneGraph(Node1)
print(result.val) # Expected 1
print(result.neighbors[0].val) # Expected 2
print(result.neighbors[1].val) # Expected 4
print(result.neighbors[0].neighbors[0].val) # Expected 1
print(result.neighbors[0].neighbors[1].val) # Expected 3
print(result.neighbors[1].neighbors[0].val) # Expected 2
print(result.neighbors[1].neighbors[1].val) # Expected 4
print(result.neighbors[0].neighbors[0].neighbors[0].val) # Expected 1
print(result.neighbors[0].neighbors[0].neighbors[1].val) # Expected 3
# Expected graph:
# 1----2
# |    |
# |    |
# 4----3
# We have to return the node with value 1
# The neighbors of 1 are 2 and 4
# The neighbors of 2 are 1 and 3
# The neighbors of 3 are 2 and 4
# The neighbors of 4 are 1 and 3