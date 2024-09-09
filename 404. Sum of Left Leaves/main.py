#Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        sum = 0

        if root.left:
            if self.isLeaf(root.left):
                sum += root.left.val
            sum += self.sumOfLeftLeaves(root.left)

        sum += self.sumOfLeftLeaves(root.right)

        return sum

    def isLeaf(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        return False



# Test cases
s = Solution()
Node1 = TreeNode(3)
Node2 = TreeNode(9)
Node3 = TreeNode(20)
Node4 = TreeNode(15)
Node5 = TreeNode(7)
Node1.left = Node2
Node1.right = Node3
Node3.left = Node4
Node3.right = Node5
print(s.sumOfLeftLeaves(Node1)) # Expected 24
