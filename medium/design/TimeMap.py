""""
981. Time Based Key-Value Store

1. click a map of lists
2. append value to key's list
3. binary search for a value in the list if its <= given timestamp

RunTime : O(1) in set
          O(logn) in get

""""



class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        
        if key not in self.m:
            x = [(timestamp,value)]
            self.m[key] = x
        
        else:
            
            self.m[key].append((timestamp,value))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        
        if key in self.m:
            
            x = self.m[key]
            
            l = 0
            r = len(x)

            while l<r:
                
                mid = (l+r)/2
                
                if x[mid][0] == timestamp:
                    return x[mid][1]
                elif x[mid][0] > timestamp:
                    r = mid-1
                else:
                    l = mid+1
            
            
            if x[mid][0] <= timestamp:
                return x[mid][1]
            if mid-1 >=0 and x[mid-1][0]<=timestamp:
                return x[mid-1][1]
                
              
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
