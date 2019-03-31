"""
144. Binary Tree Preorder Traversal

 Steps:
 
 1. Add root to stack
 2. until length of stack is greater than zero, do:
      1. curr = pop
      2. add curr.val to result
      3. push curr.right to stack
      4. push curr.left to the stack
      
      
      RunTime : O(N)

"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        r = []
        stack = [root]
        
        while len(stack)>0:
            
            curr = stack.pop()
            
            if curr:
                r.append(curr.val)
                stack.append(curr.right)
                stack.append(curr.left)
        
        return r
