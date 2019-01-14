"""
#341 : Flatten Nested List iterator


"""

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        
        self.stack = nestedList[::-1]
        
    def next(self):
        """
        :rtype: int
        """
 
        return self.stack.pop()
              
    def hasNext(self):
        """
        :rtype: bool
        """
        
        while len(self.stack)>0:
            
            if self.stack[-1].isInteger():
                
                return True
            
            else:
                
                temp=self.stack.pop()
                
                for x in temp.getList()[::-1]:
                    
                    self.stack.append(x)
                

        return False
