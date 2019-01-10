
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        self.s=""
        
        def preOrder(root):
            if root:
                self.s=self.s+str(root.val)+","
                preOrder(root.left)
                preOrder(root.right)
            else:
                self.s=self.s+"$$"+","
        
        preOrder(root)
        
        return (self.s[:-1])
        
    def deserialize(self, data):
        
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data= (data.split(","))
        
        self.index=0
        
        def preOrderArray():
            

            #Base case
            if self.index >=len(data) or data[self.index]=='$$':
                self.index+=1
                return None
            
            root = TreeNode(int(data[self.index]))
            self.index+=1
            
            root.left = preOrderArray()
            root.right = preOrderArray()
            
            return root
        
        return preOrderArray()
