"""
144. Binary Tree Preorder Traversal

Iterative

1. add curr to stack
2.    while curr has left , keep add to stack
3.    if not, 
         pop stack
         curr.val to result
         curr = curr.right
 

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        st = []
        res = []
        
        curr = root
        
        while curr or st:
            
            while (curr):
                st.append(curr)
                curr = curr.left
            
            curr = st.pop()
            res.append(curr.val)
            curr = curr.right
        
        return res
