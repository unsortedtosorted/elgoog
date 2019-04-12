"""

449. Serialize and Deserialize BST

""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.r = None
        
        if not root:
            return ""
        
        def pre(root):
            
            if root:
                
                if self.r:
                    self.r+= " "+str(root.val)
                else:
                    self.r = str(root.val)
                
                pre(root.left)
                pre(root.right)
                
                
            else:
                
                self.r+= " $"
        
        pre(root)
        return self.r

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        
        data = deque(data.split(" "))

        def pre():
            
            if data:
                
                if data[0] == '$':
                    data.popleft()
                    return None
                else:
                    root = TreeNode(data[0])
                    data.popleft()
                    root.left = pre()
                    root.right = pre()
                    
                    return root
        
        
        return pre()
