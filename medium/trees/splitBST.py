"""
776. Split BST

1. Either split right subtree or left subtree on each step
2. right subtree is split if curr value is less than or equal to the val
  2.1 change right subtree to be equal to the left of split
  2.2 return root and right subtree
3. left subtree is split if curr value is greater than the val
  3.1 change left subtree to be equal to right of split
  3.2 return left and root
  
  




"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        
        #This method returns the left and right subtrees
        def split(root):
            
            if not root:
                return None,None
            
            #if root is less than equal to V, that means all values to left 
            #dont need to be touched, only right needs to be touched because
            #some values in right may be greater or less than V
            
            elif root.val<=V:
                temp = split(root.right)
                root.right = temp[0]
                return root,temp[1]
            #if root is greater than val, then right does not need to be touched
            #only left needs to be touched since some values in left may be greater
            #or less than val
            else:
                temp = split(root.left)
                
                root.left = temp[1]
                
                return temp[0],root
        
        return split(root)
