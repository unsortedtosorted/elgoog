class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        
        self.m={}
        self.l=[]
        self.capacity=capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.m:
            self.updateq(key)
            return self.m[key]
        
        return -1
            

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        
        self.m[key]=value
        self.updateq(key)
    
    def updateq(self,key):
        
        if key in self.l:
            self.l.remove(key)
        
        self.l.append(key)
        
        if len(self.l)==self.capacity+1:
            k=self.l[0]
            del self.m[k]
            self.l=self.l[1:]
    
            
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
