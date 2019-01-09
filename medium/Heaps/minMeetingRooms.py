# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        
        if len(intervals)==0:
            return 0
        def fun(x):
            return x.start
        
        intervals=sorted(intervals,key=fun)
        
        freeRooms=[]
        
        heapq.heappush(freeRooms, intervals[0].end)
        
        for x in intervals[1:]:
            
            if x.start>=freeRooms[0]:
                heapq.heappop(freeRooms)
            
            heapq.heappush(freeRooms, x.end)
            
        
        
        return len(freeRooms)
