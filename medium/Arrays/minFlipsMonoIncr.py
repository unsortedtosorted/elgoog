class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        
        ones = 0
        zeros = 0
        
        for x in S:
            
            if x == '0':
                ones = min(ones,zeros)+1
            else:
                ones = min(ones,zeros)
                zeros+=1
        
        
        return min(ones,zeros)
