"""
369. Plus One Linked List

1. add all nodes to the stack except for last
2. add 1 to the last node
3. if greater than 9:
  3.1 make it zero
  3.2 get next node from stack, add 1
  go back to 3 keep doing until stack len, greater than 
  
  Run time : O(N)
  space : O(N)

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        stack = []
        
        temp = head
        
        while temp and temp.next:
            stack.append(temp)
            temp = temp.next
        
        
        temp.val +=1
        
        while temp.val > 9:
            if len(stack)>0:
                temp.val = 0
                temp = stack.pop()
                temp.val+=1
            else:
                break
                
        
        if temp.val > 9:
            newhead = ListNode(1)
            temp.val = 0
            newhead.next = temp
            return newhead
        else:
            return head
            
