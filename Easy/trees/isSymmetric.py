"""

101. Symmetric Tree

1. Do BFS
2. add child nodes to respective levels
3. check each level for mirror reflection


NOTE : check recursive solution on leetcode
"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        levels = {}
        
        q = deque([(root,0)])
        
        while len(q) > 0:
            
            curr = q.pop()
            
            
            curr_node = curr[0]
            curr_level = curr[1]
            
            lval = "$"
            rval = "$"
            if curr_node.left:
                lval = curr_node.left.val
                q.appendleft((curr_node.left,curr_level+1))

            if curr_level in levels:
                levels[curr_level].append(lval)
            else:
                levels[curr_level] = [lval]
            
            if curr_node.right:
                rval = curr_node.right.val
                q.appendleft((curr_node.right,curr_level+1))
            
            levels[curr_level].append(rval)
        
        
        
        
        def check(arr):
            
            p1 = 0
            p2 = 0
            
            if len(arr)%2 == 0:
                p2 = len(arr)//2
                p1 = p2-1
            else:
                p1 = len(arr)//2
                p2 = p1
                
            
            while p1 > -1 and p2 < len(arr):
                
                if arr[p1] != arr[p2]:
                    return False
                
                p1-=1
                p2+=1
            
            return True
        
        for x in levels:
            
            if not check(levels[x]):
                return False
        
        return True
                
            
