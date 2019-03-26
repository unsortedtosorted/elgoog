"""
729. My Calendar I

1. add item to calendar if no collision with any existing entries
2. to check for confict:
    1. a starts before b ends and aends after b starts


"""

class MyCalendar(object):

    def __init__(self):
        self.start = None
        self.stop = None
        self.intervals = []
        

    def book(self, start, stop):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        
        for x in self.intervals:
            
            # A and B start/stop at same time
            
            if  start < x[1]  and x[0]<stop:
                return False
            
            
            
        self.intervals.append([start,stop])
        
        self.intervals = sorted(self.intervals, key = lambda x: x[0])
        return True
                
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
