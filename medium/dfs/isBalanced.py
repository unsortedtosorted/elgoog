"""
#110 Balanced Binary Tree

1. Get length of left child
2. Get legth of right child
3. if difference is less than equal to 1 update answer
4. return max of left or right tree height+1

Run Time : O (N)

"""


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        self.l = True
        def getlen(root):
            
            if root:
                
                l = getlen(root.left)
                r = getlen(root.right)
                
                if abs(l-r)>1:
                    self.l = self.l and False
                else:
                    self.l = self.l and True
                
                return max(l,r)+1
            
            else:
                
                return 0
        getlen(root)
        
        return self.l
