"""

DP equation :   

    getCost(i,m) = min of (costs[i][n]+getCost(i+1,n))  for all colors and where n!=m
		getCost(i,m) : min cost of painting ith houst if last house is painted with m
    
"""
						

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0:
            return 0
        memo = {}
        def getCost(currind, lastColorInd):
            
            if currind == len(costs):
                return 0
            
            if (currind, lastColorInd) in memo:
                return memo[(currind, lastColorInd)]

            c,i = sys.maxsize,0
            
            while i < len(costs[currind]):
                
                if i!= lastColorInd:
                    c = min(c, costs[currind][i]+getCost(currind+1,i))
                    
                i+=1
            memo[(currind, lastColorInd)] = c
            return c
        
        return getCost(0,-1)  
