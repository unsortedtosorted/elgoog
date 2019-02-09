"""

426. Convert Binary Search Tree to Sorted Doubly 

1. Traverse the binary tree to get the sorted items and store then in array : O(N)
2. create head from 0th element, make it prev
3. start iterating over the array from the 1st element, 
    3.1 currNode = node(i)
    3.2 currNode.left = prev
    3.3 prev = currNode
4. currNode.right = head
5. head.left = currNode

Runtime : O(N) + O(N) = O(N)
space  : O(N)


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
                inOrder(root.left)
                self.arr.append(root.val)
                inOrder(root.right)
        
        inOrder(root)
        
        if len(self.arr)==0:
            return None
        
        head = Node(self.arr[0],None,None)
        
        
        prev = head
        curr = None
        
        for i,x in enumerate(self.arr[1:]):
            
            curr = Node(x,prev,None)
            prev.right = curr
            prev = curr
        
        if curr:
            curr.right = head
            head.left = curr
        else:
            head.left = head
            head.right = head
        
        return head
