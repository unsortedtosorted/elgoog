class Solution:
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        
        r = []
        
        def generatePairs(n,r):
            i=1
            end=n
            
            while i<end:
                r.append("("+str(i)+","+str(end)+")")
                i+=1
                end-=1
        
        generatePairs(n,r)
        
        while n>2:
            
            start=0
            stop=len(r)-1
            temp=[]
            while start<stop:
                
                t1=r[start]
                t2=r[stop]
                
                temp.append("("+str(t1)+","+str(t2)+")")
                start+=1
                stop-=1
                
            
            r=temp
            n=n/2

        return (str(r[0]))
