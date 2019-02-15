"""
142. Linked List Cycle II


"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        seen = set ()
        temp = head
        found = None
        
        while temp :
            
            if temp in seen:
                found = temp
                break
            
            seen.add(temp)
            temp = temp.next

        return found
