class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        
        rep = math.ceil(len(B)/len(A))
        
        if B in A*rep:
            return rep
            
        elif B in A*(rep+1):
            return rep+1
        else:
            return -1
