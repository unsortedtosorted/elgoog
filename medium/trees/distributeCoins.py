"""

Algo :

1. If not node, moves = 0
2. if node , moves = moves from left subree + modes from right subtree
3. return node.val + L + R -1

Run time : O(N)

"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        
        def dfs(root):
            
            if not root:
                return 0
            
            else:
                
                #get excess coins from left
                L = dfs(root.left)
                
                #get excess coing from the right
                R = dfs(root.right)
                
                self.ans += abs(L) + abs(R)
                
                return root.val + L + R -1
        
        dfs(root)
        return self.ans
