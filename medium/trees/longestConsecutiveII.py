"""
549. Binary Tree Longest Consecutive Sequence II

Algo: 
  1. for each node maitain 2 values:
      increment_sequence
      decerement_sequence
  2. if child is curr+1:
          increment_sequence = child's increment sequence + 1
     if child is curr-=1:
          decerement_sequence = child's decerement_sequence - 1
     
     return max of increment_sequence+decerement_sequence-1  from each node
     
        

"""


class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        m = [0]
        def getpath(root):
            
            inc,dec = 1,1
            
            if root:
                incr,decr = 0,0
                incl,decl = 0,0
                
                if root.left :
                    incl,decl = getpath(root.left)
                    
                    if root.left.val == root.val+1:
                        inc = incl+1
                    elif root.left.val+1 == root.val:
                        dec = decl+1
                    
                if root.right:
                    incr,decr = getpath(root.right)
                    
                    if root.right.val == root.val+1:
                        inc = max(inc,incr+1)
                    elif root.right.val+1 == root.val:
                        dec = max(dec,decr+1)
            
                m[0] = max(m[0],inc + dec - 1)
                
                return inc,dec
        
        getpath(root)
        
        return m[0]
