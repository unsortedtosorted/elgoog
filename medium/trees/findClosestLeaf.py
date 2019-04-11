"""
742. Closest Leaf in a Binary Tree


1. find the closes child leaf from each node and its level
2. now travel all nodes again, let them know their parent, check if parent level+1 < child level+1


runtime : O(N)
space : O(N)

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        m = {}
        
        def getnearestChildLeaf(root,level):
            
            if root:
                
                if not root.left and not root.right:
                    m[root.val] = (root.val,level)
                    return (root.val,level)
                else:
                    l,r = None,None
                    if root.left:
                        l = getnearestChildLeaf(root.left,level+1)
                    if root.right:
                        r = getnearestChildLeaf(root.right,level+1)
                        
                    if r and l:
                        if r[1] < l[1]:
                            m[root.val] = r
                            return r
                        else:
                            m[root.val] = l
                            return l
                    elif r and not l:
                        m[root.val] = r
                        return r
                    else:
                        m[root.val] = l
                        return l
        def inorder(root):
            
            if root:
                inorder(root.left)
                getnearestChildLeaf(root,0)
                inorder(root.right)
        
        inorder(root)
        print (m)
        re = [None]
        def find(root,parent):
            
            if root:
                
                if root.val == k:
                    
                    if m[parent.val][1]+1 < m[root.val][1]:
                        re[0] = m[parent.val][0]
                    else:
                        re[0] = m[root.val][0]
                    
                else:
                    
                    
                    find(root.left,root)
                
                    find(root.right,root)
        
        
        
        find(root,root)
        return re[0]
        
