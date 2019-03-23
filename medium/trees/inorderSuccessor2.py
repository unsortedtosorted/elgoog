"""

510. Inorder Successor in BST II

Given a node, return the next inorder node 

1. if right node is present, return the left most child of right node

2. if right node is not present,
   --keep getting the parent until parent.val is not greater than node.val
   
   
   RunTime : Log(N)


"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""
class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        temp = None
        if node.right:
            temp = node.right
            while temp.left:
                temp = temp.left
        else:
            
            if node.parent:
                
                temp = node.parent
                
                while temp and temp.val<node.val:
                    temp = temp.parent
        
        
        return temp
