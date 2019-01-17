class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.lev = 0
        def preOrder(root,level):
            
            
            
            if root:
                if level>self.lev:
                    self.lev=level
                if root.left: 
                    if root.left.val==root.val+1:
                        preOrder(root.left,level+1)
                    else:
                        preOrder(root.left,1)
                
                if root.right:
                    if root.right.val==root.val+1:
                        preOrder(root.right,level+1)
                    else:
                        preOrder(root.right,1)
                
                
                
                    
        preOrder(root,1)
        
        return self.lev
