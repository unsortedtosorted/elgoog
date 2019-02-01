"""
281. Zigzag Iterator



"""

from collections import deque
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        
        self.q = deque()
        v1 = v1[::-1]
        v2 = v2[::-1]
        while len(v1)>0 and len(v2)>0:
            self.q.append(v1.pop())
            self.q.append(v2.pop())
        
        if len(v1)>0:
            while len(v1)>0:
                self.q.append(v1.pop())
        else:
            while len(v2)>0:
                self.q.append(v2.pop())
                
        print (self.q)

    def next(self):
        """
        :rtype: int
        """
        return self.q.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.q)>0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
