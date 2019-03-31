"""
563. Binary Tree Tilt 

1. get left tree sum
2. get right tree sum
3. add to total abs(lsum - rsum)
4. return r + lsum + rsum

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        result = [0]
        def getSum(root):
            
            if root:
                
                l = getSum(root.left)
                r = getSum(root.right)
                
                currTilt = abs( l - r )
                
                result[0] += currTilt
                
                return root.val + l + r
                
                
            
            
            else:
                return 0
        
        getSum(root)
        return result[0]
