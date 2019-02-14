"""
374. Guess Number Higher or Lower

"""

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        start = 1
        stop = n
        
        while start<=stop:
            mid = (start+stop)//2
            x = guess(mid)
            if  x == 0:
                return mid
            elif x == -1:
                stop = mid-1
            else:
                start = mid+1
        
        return -1
