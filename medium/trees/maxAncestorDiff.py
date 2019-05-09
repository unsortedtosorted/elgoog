"""
1026. Maximum Difference Between Node and Ancestor

1. return min,max value seen till now
2. update max diff to be max of abs with min and max value

runtime : O(N)

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        self.val = -sys.maxsize-1
        
        def dfs(root):
            
            if root:
                
                if not root.left and not root.right:
                    return root.val,root.val
                
                new_min = sys.maxsize
                new_max = -sys.maxsize-1
                
                if root.left:
                    
                    mi1,ma1 = dfs(root.left)
                    v1 = abs(root.val - mi1)
                    v2 = abs(root.val - ma1)
                    
                    self.val = max(self.val,v1)
                    self.val = max(self.val,v2)
                    
                    new_min = min(root.val,mi1)
                    new_max = max(root.val,ma1)
                
                
                if root.right:
                    mi2,ma2 = dfs(root.right)
                    v3 = abs(root.val - mi2)
                    v4 = abs(root.val - ma2)
                    self.val = max(self.val,v3)
                    
                    self.val = max(self.val,v4)
                
                    new_min = min(new_min,mi2)
                    new_max = max(new_max,ma2)
                
                return min(root.val,new_min),max(root.val,new_max)
        
        dfs(root)
        
        return self.val
                    
                    
