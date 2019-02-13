"""
113. Path Sum II

Algo:
1. Go to root, subtract its val from total
2. call left child with new total and prev path
3. call right child with new total and prev path
4. pop root from path

memory : O(1)
run time : O(N)


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        self.out = []
        def dfs(root,total,path):
            
            if root:
                
                total -=root.val
                
                path.append(root.val)
                
                if total == 0 and root.left == None and root.right == None:
                    self.out.append(list(path))
                if root.left:
                    dfs(root.left,total,path)
                
                if root.right:
                    dfs(root.right,total,path)
                path.pop()
        
        dfs(root,sum,[])
        
        return self.out
