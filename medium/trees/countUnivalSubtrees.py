"""
250. Count Univalue Subtrees

"""

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
                    
        def backTrack (root):
            
            l = True
            r = True
            if root:
                
                if not root.left  and not root.right:
                    self.count+=1
                    return True
                
                else:
                    
                    if root.left:
                        
                        l = backTrack (root.left)
                        
                        if root.val != root.left.val:
                            l = False
 
                    if root.right:
                        
                        r =backTrack (root.right)
                        
                        if root.val != root.right.val:
                            r = False
                    
                    if l&r:
                        self.count+=1
                    
                    return l&r
                   
        backTrack (root)
        
        return self.count
