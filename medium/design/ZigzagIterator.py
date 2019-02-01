"""
281. Zigzag Iterator



"""

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        
        self.i=0
        self.j=0
        self.v1=v1
        self.v2=v2
        self.lastv1=False
        
        

    def next(self):
        """
        :rtype: int
        """
        if self.lastv1:
            if self.j<len(self.v2):
                temp = self.v2[self.j]
                self.j+=1
               
            else:
                temp = self.v1[self.i]
                self.i+=1
            self.lastv1=False    
            return temp
        else:
            if self.i<len(self.v1):
                temp = self.v1[self.i]
                self.i+=1
                
            else:
                temp = self.v2[self.j]
                self.j+=1
                

            self.lastv1=True
            return temp
            
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i<len(self.v1) or self.j<len(self.v2)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
