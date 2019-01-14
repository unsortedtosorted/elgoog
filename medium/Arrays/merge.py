class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        intervals=sorted(intervals, key = lambda x: x.start)
        
        if len(intervals)==0:
            return intervals

        prev = intervals[0]
        r = []
        
        i=1
        
        while i<len(intervals):
            
            curr = intervals[i]
            
            if curr.start<= prev.end:
                #overlap
                
                prev = Interval(prev.start,max(prev.end,curr.end))
            else:
                r.append(prev)
                prev=curr
            i+=1
        r.append(prev)
        
        return r
