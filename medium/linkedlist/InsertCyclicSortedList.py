"""

708. Insert into a Cyclic Sorted List

1. for 2 nodes curr and next , if insert val is between them , insert new node.
2. if not, insert between max and minNode




# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        
        if not head:
            
            head = Node(insertVal,None)
            head.next = head
            return head
        
        if not head.next:
            
            temp = Node(insertVal,None)
            
            temp.next = head
            head.next = temp
            
            return head
        
        #generic
        
        temp = head
        nex = temp.next
        
        maxNode = temp
        minNode = nex
        
        while not (temp.val <= insertVal and insertVal <= nex.val):
            
            if temp.val >= maxNode.val:
                maxNode = temp
            if nex.val >= maxNode.val:
                maxNode = nex
            
            if temp.val <= minNode.val:
                minNode = temp
            
            if nex.val <= minNode.val:
                minNode = nex
            
            temp = nex
            nex = temp.next
            
            
            
            if temp == head:

                newNode = Node(insertVal,None)
                if maxNode.val == minNode.val:
                    minNode = maxNode.next
                maxNode.next = newNode
                newNode.next = minNode
                
                return head
                

        new = Node(insertVal,None)
        
        temp.next = new
        new.next = nex

        return head
                
