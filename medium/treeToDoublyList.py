"""
426. Convert Binary Search Tree to Sorted Doubly 

# create doubly ll
1. l= get right most node from left subtree
2. r= get left most node from right subtree
3. curr.left = l, curr.right = r, return right

#attach head to end and end to head
1. iterate to left most node of end node
2. leftmode.left = end
3. end.right = leftmostnode
4. return leftmodestnode

RunTime: O(N)
Space : O(1)


# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        self.arr = []
        
        def inOrder(root):
            
            if root:
                
                middle = Node(root.val,None,None)
                
                left = inOrder(root.left)
                temp = left
                
                #get right  most of left subtree
                while temp and temp.right:
                    temp = temp.right
                
                if temp:
                    middle.left = temp
                    temp.right = middle
                
                right = inOrder(root.right)
                temp = right
                
                #get left most of right subtree
                while temp and temp.left:
                    temp = temp.left
                
                
                if temp:
                    middle.right = temp
                    temp.left = middle
                    
                    return right
                
                
                
                return middle
            
            else:
                return None
        

        end = inOrder(root)
        
        if not end:
            return None
        temp = end
        
        while temp.left:
            
            temp = temp.left
        
        if temp:
            temp.left = end
            end.right = temp
            return temp
        else:
            end.left = end
            end.right = end
            return end
            
