"""
112. Path Sum

if leaf node reached , return true if remain is zero else return false
if not leaf node, return 'or' of left and right subtree 

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        def checkVal(root,remain):
            
            if root:
                
                if not root.left and not root.right:
                    if remain-root.val == 0:
                        return True
                    else:
                        return False
                else:
                    
                    return checkVal(root.left,remain-root.val) or checkVal(root.right,remain-root.val)
            else:
                return False
