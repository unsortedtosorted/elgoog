# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
"""

Time limit exceeded :
  Time complexity : O(nLogN+N*N) = O (N^2)

"""
class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        def fun(x):
            return x.start
        
        intervals=sorted(intervals,key=fun)
        
        def canfit(time,room):
            for usedtimes in room:
                #check before and after
                if not (time.end<=usedtimes.start) and not (time.start>=usedtimes.end):
                    return False
            return True
        
        rooms=[]
        
        if len(intervals)<1:
            return 0
        rooms.append([intervals[0]])
        
        
        for x in intervals[1:]:
            found=False
            for i,y in enumerate(rooms):
                if canfit(x,y):
                    rooms[i].append(x)
                    found=True
                    break
            
            if not found:
                rooms.append([x])
        
        return len(rooms)
