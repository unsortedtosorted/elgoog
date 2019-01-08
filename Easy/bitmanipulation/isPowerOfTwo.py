"""
#231 : Check if power of 2

  A number is power of two if there is only single
  1 in it.
  
  to find out if number of one is more than ,equal to 1:
    n&(n-1)
    
    e.g 1000&111=0
        1010& 1001!=0 

"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
      
        
        if n<=0:
            return False
        
        return (n&(n-1))==0
                
