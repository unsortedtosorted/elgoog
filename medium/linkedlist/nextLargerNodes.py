"""
1030. Next Greater Node In Linked List

1. Create an array , add all elemts to it
2. traverse from reverse
3. add item to list if last element greater than it
4. else:
      keep removing element from the list until last element is greater or the lenght of stack is greater than 0



"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import deque

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        l = []
        
        st = []

        temp = head
        
        while temp:
            l.append(temp.val)
            temp = temp.next
        st.append(l[-1])
        r = [0]*len(l)
        i = len(l)-2
    
        while i >=0:
       
            if l[i] < st[-1]:
                r[i] = st[-1]
                st.append(l[i])
            else:
                while len(st) > 0:
                    if st[-1] <= l[i]:
                        st.pop()
                    else:
                        break
                if len(st)>0:
                    r[i] = st[-1]
                else:
                    r[i] = 0
                st.append(l[i])
            i-=1
        return r
