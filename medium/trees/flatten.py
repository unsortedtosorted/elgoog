"""
114. Flatten Binary Tree to Linked List

Steps:

if leaf node, do nothing
if not leaf node:
  flatten left subtree
  flatten right subtree
  connect right child to right most leaf of left child
  make left child as right child
  make left child None

  RunTime : O(N^2)
  Space : O(N)
"""


class Solution(object):
    def flatten(self, root):
        
        def convert(root):
            
            if root:
                
                if not root.left and not root.right:
                    return
                
				#flatten left and right child
                convert(root.left)
                convert(root.right)
                
                l = root.left
                r = root.right
                
				#make left child as new right child
                root.right = l
                root.left = None
			    
                temp = root
                #get right most leaf of new right child
                while temp.right:
                    temp = temp.right
                
                temp.right = r
        
        convert(root)
