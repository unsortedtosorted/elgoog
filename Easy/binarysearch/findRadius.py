class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        

        heaters.sort()
        r = []
        
        for i,x in enumerate(houses):
            
            start=0
            stop=len(heaters)-1
            mid = (start+stop)//2
            dis = sys.maxsize
            
            while start<=stop:
               
                mid = (start+stop)//2
                if abs(x-heaters[mid])<dis:
                    dis=abs(x-heaters[mid])
                
                if heaters[mid] == x:
                    break
                elif heaters[mid] > x:
                    stop = mid -1
                    
                elif heaters[mid] < x:
                    start = mid+1
            r.append(dis)
        
        
        return max(r)
            
