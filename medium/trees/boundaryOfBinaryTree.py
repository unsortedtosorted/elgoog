# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.r = []
        self.rt = []
        def getleftbound(root):
            
            if root:
                if root.left:
                    self.r.append(root.val)
                    getleftbound(root.left)
                    return
                if root.right:
                    self.r.append(root.val)
                    getleftbound(root.right)
                    return
                    
        
        def getleaves(root):
            
            if root:
                
                if not root.left and not root.right:
                    self.r.append(root.val)
                
                if root.left:
                    getleaves(root.left)
                if root.right:
                    getleaves(root.right)
        
        def getrightbound(root):
            
            if root :
                
                if root.right:
                    self.rt = [root.val]+self.rt
                    
                    getrightbound(root.right)
                    return 
                if root.left:
                    self.rt = [root.val]+self.rt
                    getrightbound(root.left)
                    
                    
                    
        
        if root:
            self.r.append(root.val)
            getleftbound(root.left)
            if root.left or root.right:
                getleaves(root)
            getrightbound(root.right)
            self.r+=self.rt
        return self.r
