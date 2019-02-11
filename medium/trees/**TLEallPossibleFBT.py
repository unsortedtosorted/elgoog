# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        
        if N%2 ==0:
            return []
        
        def createcopy(root,newhead):
            
            if root:
                
                if root.left:
                    newhead.left = TreeNode(root.left.val)
                    createcopy(root.left,newhead.left)
                if root.right:
                    newhead.right = TreeNode(root.right.val)
                    createcopy(root.right,newhead.right)
            
       
        def bfs (root):
            
            q = deque()
            r = []
            if not root:
                return []
            q.appendleft(root)
            
            
            while len(q)>0:
                
                tempnode = q.pop()
                
                if tempnode:
                    q.append(tempnode.left)
                    q.append(tempnode.right)
                    r.append("0")
                    
                
                else:
                    r.append("null")
            
            return r
                    
                    
            
        def addtoleaves(root):
            
            q = deque()
            
            if not root:
                return 0
            q.appendleft(root)
            temp = 0
            
            r = []
            while len(q)>0:
                
                tempnode = q.pop()
                
                if not tempnode.left and not tempnode.right:
                    tempnode.left = TreeNode(0)
                    tempnode.right = TreeNode(0)
                    newhead = TreeNode(root.val)
                    createcopy(root,newhead)
                    
                    r.append(newhead)
                    tempnode.left = None
                    tempnode.right = None
                    
                    
                elif tempnode.left and not tempnode.right:
                    q.pushleft(tempnode.left)
                elif not tempnode.left and tempnode.right:
                    q.pushleft(tempnode.right)
                else:
                    q.appendleft(tempnode.left)
                    q.appendleft(tempnode.right)
            
            
            return r
        
        def removedups(k):
            out = []
            seen =  set()
            for x in k:
                temp = tuple(bfs(x))
                if temp not in seen:
                    seen.add(temp)
                    out.append(x)
            
            return out
            
        
        def getBase(N):
            r = []
            if N>1:
                l = getBase(N-2)
                for x in l:
                    r = r + addtoleaves(x)
                    rsub = removedups(r)
                return rsub
                    
            else:
                return [TreeNode(0)]
        
       
               
        k = getBase(N)        
        return k
