"""
951. Flip Equivalent Binary Trees

Algorithm :

Can be broken into 2 subcases:
  1. Node is flipped
  2. Node is not flipped
  
  When node is not flipped left subtree of root1 is eqaul to left subtree of root2 , similarly for right
  when node is flipped the left subtree of root1 is equal to right subtree of root2 and vice versa
  
  
  Psuedocode:
  def dfs:
    if root1 and root2:
      if root1=root2:
          
          return (dfs(root1.left,root2.left) and dfs(root1.right,root2.right)) or 
          (dfs(root1.left,root2.right) and dfs(root1.right,root2.left))

      else:
        return False
    elif not root1 and not root2:
      return True
     
    else:
    return False
    
  

"""


class Solution:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        
        def dfs(r1,r2):
            
            if r1 and r2:
                
                if r1.val==r2.val:
                    return ( dfs(r1.left,r2.left) and dfs(r1.right,r2.right)) or ( dfs(r1.left,r2.right) and dfs(r1.right,r2.left)) 

                else:
                    return False
                
            elif not r1 and not r2:
                return True
            
            else:
                return False

        return dfs(root1,root2)
