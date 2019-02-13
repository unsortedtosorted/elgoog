"""
116. Populating Next Right Pointers in Each Node

while root and root.left:
  1. connect left to root to right of root
  2. connect right of root to next of roots left

do it bfs

runtime : o(n)
space : o(1)

"""



# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from collections import deque

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        
        order = deque()

        
        if not root:
            return root
        
        order.appendleft((root,0))
        
        l =[(order[0])]
        
        while len(order)>0:
            
            c = order.pop()
            curr = c[0]
            level = c[1]
            
            
            if curr.left:
                order.appendleft((curr.left,level+1))
                l.append((curr.left,level+1))
            if curr.right:
                order.appendleft((curr.right,level+1))
                l.append((curr.right,level+1))
                
        prev = l[0]
        
        for x in l[1:]:
        
            prevl = prev[1]
            currl = x[1]
            if prevl == currl:
                prev[0].next = x[0]
            
            prev = x
        
