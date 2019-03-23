"""

931. Minimum Falling Path Sum

 For each dp(row,col) = A[row][col] + min(dp(row+1,col),dp(row+1,col-1),dp(row+1,col+1))

"""


class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        memo = {}
        def getMax(row,col):

            if (row,col) in memo :
                return memo[(row,col)]
            if row == len(A)-1:
                
                return A[row][col]
            else:
                
                l = sys.maxsize
                r = sys.maxsize

                if col-1>=0:
                    l = getMax(row+1,col-1)
                
                if col+1<len(A[row]):
                    r = getMax(row+1,col+1)
                
                curr = getMax(row+1,col)
                
                temp = A[row][col]+min(l,curr,r)
                
                memo[(row,col)] = temp
                
                return temp
        r = sys.maxsize   
        
        for i,x in enumerate(A):
            r= min(r,(getMax(0,i)))
        
        return r 
            
