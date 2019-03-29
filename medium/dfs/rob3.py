"""

337. House Robber III

if Parent is robbed we have only 1 option
    -- Donot rob current node

if parent is not robbed we have 2 options
    option 1: Rob current node
    option 2 : Do not rob current node
        -- we return max (option 1, option 2 )

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        memo = {}
        def robsum(parentRobbed, root):
            
            if not root:
                return 0
            
            if (parentRobbed, root) in memo :
                
                return memo[(parentRobbed, root)]

            #if parent is robbed we have one option
            if parentRobbed:
                
                x = robsum(False, root.left)+robsum(False, root.right)
                memo[(parentRobbed, root)] = x
                return  memo[(parentRobbed, root)]
            
            #if parent is not robbed we have 2 options
            else:
                robParent = root.val + robsum(True, root.left)+robsum(True, root.right)
                robChild = robsum(False, root.left)+robsum(False, root.right)
                memo[(parentRobbed, root)] = max(robParent,robChild)
                return memo[(parentRobbed, root)]

        return robsum(False, root)
            
            
