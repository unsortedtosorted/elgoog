from collections import deque

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        
        powers =[]
        i = 1
        
        while i*i<=n:
            powers.append(i*i)
            i+=1
        
        
        toCheck = deque()
        toCheck.appendleft(n)
        seen = set()
        level = 1
        
        lev = {}
        lev[n]=1
        
        while len(toCheck)>0:
            

            temp=toCheck.pop()
            level=lev[temp]
            if temp in seen:
                continue
            else:
                
                seen.add(temp)
                for x in powers:
                    if temp-x in lev:
                        continue
                    else:
                        if x==temp:
                            return lev[x]
                        elif x<temp:
                            toCheck.appendleft(temp-x)
                            lev[temp-x]=level+1
