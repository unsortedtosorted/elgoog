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
        
        self.data=[]
        x=-1
        for x in range(0,min(len(v1),len(v2))):
            self.data.append(v1[x])
            self.data.append(v2[x])
        
        if x == len(v1)-1:
            for y in range(x+1,len(v2)):
                self.data.append(v2[y])
        else:
            for y in range(x+1,len(v1)):
                self.data.append(v1[y])
        
        self.iter=0
            
        
        

    def next(self):
        """
        :rtype: int
        """
        temp= self.data[self.iter]
        self.iter+=1
        return temp
            
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.iter<len(self.data)
