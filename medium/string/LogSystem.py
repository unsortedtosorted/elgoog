"""
635. Design Log Storage System

1. put a timestamp,id return id's that fall in range start and stop
2. convert the time to int, such that:
  2.1 0 -> time in year
  2.2 1 -> time in year+month
  2.3 2 -> time in year+month+day ...

3. convert the start and stop time to number
4. fetch index from list that maps to granularity i.e,if 
  4.1 gran = Year, return 1
  4.2 gran = Month, return 2
  4.3 gran = Day, return 3
  
  Run Time: Put O(1)
            Retreival O(N)


"""



class LogSystem(object):

    def __init__(self):
        self.m = {}
        self.m["Year"] = 1
        self.m["Month"] = 2
        self.m["Day"] = 3
        self.m["Hour"] = 4
        self.m["Minute"] = 5
        self.m["Second"] = 6
        
        
        self.mult = {}
        self.mult[1] = 1.0
        self.mult[2] = 12.0
        self.mult[3] = 12*30.0
        self.mult[4] = 12*30*24.0
        self.mult[5] = 12*30*24*60.0
        self.mult[6] = 12*30*24*60*60.0
        
        
        
        self.dict = {}

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        s = timestamp.split(":")[::-1]
        v = []
        temp = 0
        for x in range(1,7):
            t = s.pop()
            mult = self.mult[x]
            temp += int(t)/mult
            v.append(temp)
        
        self.dict[id] =  v
        

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        
        r = []
        
        start = self.getabs(s,gra)
        stop = self.getabs(e,gra)
        
        for x in self.dict:
            
            t = self.dict[x][int(self.m[gra])-1]
            if start<=t<=stop:
                r.append(x)
        
        return r
        

    def getabs(self,time,gra):
        
        s = time.split(":")[::-1]
        graId = self.m[gra]
        temp = 0
        
        for x in range(1,graId+1):
            t = s.pop()
            mult = self.mult[x]
            temp += int(t)/mult

        return temp
              
