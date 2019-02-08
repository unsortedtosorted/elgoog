"""
250. Count Univalue Subtrees

Algorithm:

if leaf node:
      count++
      return True
else:
  if left child is unival and right child is unival:
      if root == left and root ==right:
          count++
          return True
  else:
      return False
    
    
  Run Time: O(N)
  

"""





# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count=0
        def unival(root):
            
            if root:
                
                l = True
                
                if root.left:
                    l = unival(root.left)
                r = True
                
                if root.right:
                    r = unival(root.right)
                    
                if l and r:
                    #left anf right both exist
                    if root.left and root.right:
                        if root.val == root.left.val and root.val == root.right.val:
                            self.count+=1
                            return True
                        
                    
                    
                    #left only exist
                    if not root.right and root.left:
                        if root.left.val == root.val:
                            self.count+=1
                            return True
                    
                    
                    
                    #right only exist
                    elif not root.left and root.right:
                        if root.right.val == root.val:
                            self.count+=1
                            return True
                    
                    
                    
                    #left and right both dont exist
                    elif not root.left and not root.right:
                        self.count+=1
                        return True
                
                
                else:
                    return False
        unival(root)
        return self.count
