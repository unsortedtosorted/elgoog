"""
993. Cousins in Binary Tree


1. Store parent and level of each node

"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        
        lev = deque()
        cousinMap = {}
        
        
        lev.appendleft((root,0,None))
        
        while len(lev)>0:
            
            curr = lev.pop()
            
            node = curr[0]
            level = curr[1]
            parent = curr[2]
            
            cousinMap[node.val] = (level,parent)
            
            
            if node.left:
                 lev.appendleft((node.left,level+1,node.val))
            if node.right:
                 lev.appendleft((node.right,level+1,node.val))
        
        
        
        nodex= cousinMap[x]
        levelx = nodex[0]
        parentx = nodex[1]
        
        nodey= cousinMap[y]
        levely = nodey[0]
        parenty = nodey[1]
        
        
        if levelx == levely and parentx!=parenty:
            return True
        else:
            return False
