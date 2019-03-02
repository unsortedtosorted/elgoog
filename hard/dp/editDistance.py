"""

72. Edit Distance

dp (i,j) = min (cost of replace + dp(i+1,j+1), dp(i+1,j), dp (i,j+1))

"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        self.m = {}
        def dp(i,j):
            
            if (i,j) in self.m:
                
                return self.m[(i,j)]
            
            if i == len(word1) and j == len(word2):
                self.m[(i,j)] = 0
                return 0

            if i==len(word1):
                self.m[(i,j)] = len(word2[j:])
                return len(word2[j:])
        
            if j==len(word2):
                self.m[(i,j)] = len(word1[i:])
                return len(word1[i:])
            
            costReplace = 1
            if word1[i] == word2[j]:
                costReplace = 0
                
            
            #replace
            c2 = costReplace+dp(i+1,j+1)
            
            #insert
            c3 = 1+dp(i,j+1)
            
            #delete
            c4 = 1+dp(i+1,j)
            
            self.m[(i,j)] = min(c2,c3,c4)
            return min(c2,c3,c4)
        
        return (dp(0,0))
