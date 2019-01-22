class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        
        d = []
        
        r = []
        for i,x in enumerate(seats):
            
            if x==1 : d.append(i)
            
        
        
        if len(d)==1:
            return max(d[0],len(seats)-1-d[0])
        
        else:
            prev = 0
            r.append((d[0]-prev))
            
            prev=d[0]
            for x in d[1:]:
                r.append((x-prev)//2)
                prev = x
        
            r.append(len(seats)-1-prev)
        
        return max(r)
