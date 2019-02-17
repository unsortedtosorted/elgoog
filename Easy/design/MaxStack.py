"""
1. Max Stack

use regular stack

Find what operation is going to take place the most
for top : find max in O(N)
for popmax: find max and remove it from the stack

"""

class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.arr.append(x)

    def pop(self):
        """
        :rtype: int
        """
        r = self.arr.pop()
        return r
        

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1]
        

    def peekMax(self):
        """
        :rtype: int
        """
        
        temp = 0
        
        for i,x in enumerate(self.arr):
            
            if x>=self.arr[temp]:
                temp = i
        
        return self.arr[temp]
        

    def popMax(self):
        """
        :rtype: int
        """
        temp = 0
        
        for i,x in enumerate(self.arr):
            
            if x>=self.arr[temp]:
                temp = i
        
        val = self.arr[temp]
        del self.arr[temp]
        
        return val
