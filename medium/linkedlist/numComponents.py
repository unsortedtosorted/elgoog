"""
817. Linked List Components

1. check if curr in list and curr.next also in list, if yes continue
2. if curr in list and curr.next not in list, then count +=1
return count

Run time : O(N)

"""

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        
        
        l = set(G)
        
        count = 0
        while head:
            if head.val in l:
                if head.next==None:
                    count+=1
                elif head.next.val not in l :
                    count+=1
            head=head.next

        return count
