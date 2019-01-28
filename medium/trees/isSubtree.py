"""

#572. Subtree of Another Tree

1. Do DFS of first Tree, if node equal to root of another tree, do preorder
traversal together and return if True if traversal is same

2. if no Node is equal to root of another tree , return False

RunTime : O (N*M)



"""


class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        def dfs2(root1,root2):
            
            if root1 and root2:
                
                if root1.val == root2.val:
                    
                    return (dfs2(root1.left,root2.left) and dfs2(root1.right,root2.right))
                
                else:
                    return False
                    
                    
            elif not root1 and not root2:
                return True
            
            else:
                return False
        
        def dfs(root):
            
            if root:
                if root.val == t.val and dfs2(root,t):
                    return True
 
                else:
                    
                    return ( dfs(root.left) or dfs(root.right))
            else:
                return False
            

        return dfs(s)
        
