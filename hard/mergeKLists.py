# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """  
        
        
        l= []
        
        for x in lists:
            
            temp=x
            while temp:
                heapq.heappush(l,temp.val)
                temp=temp.next
        
        
        if len(l)==0:
            return None
        
        root=ListNode(l[0])
        heapq.heappop(l)
        temp=root
        
        
        while len(l)>0:
            
            temp.next=ListNode(heapq.heappop(l))    
            temp=temp.next
        
        return root
  
                
