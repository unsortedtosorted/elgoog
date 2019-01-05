"""
#543

1. Get the length of path of the left subtree
2. Get the lenght of path of the right subtree
3. if the left path + right path is greater than the previous max, store it
4. return maximum of left path or right path to the parent node
5. keep doing it recursively
 
  Time complexity is : O(N) 
  Space complexity is : O(1)


"""



class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.path = 0
        
        def getsubtreeheights(root):
            
            if root:
                l=getsubtreeheights(root.left)
                r=getsubtreeheights(root.right)
                
                if l+r>self.path:
                    self.path=l+r
                return max(l,r)+1
                
            else:
                return 0
            
        getsubtreeheights(root)
        return self.path
