"""
986. Interval List Intersections

1. 2 intervals intersect if start of 1 is between start and end of other
2. for 2 intervals check if a intersect b or vice versa
3. which ever is older, discard

Runtime : O(M+N)

"""


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        
        r = []
        def check(a,b):
            
            if  a.start <= b.start and b.start <= a.end:
                return True
            return False
            
        i = 0
        j = 0
        
        while i < len(A) :
            
            if j < len(B):
                
                a = A[i]
                b = B[j]

                if check(a,b):
                    #check if b's start is in between
                    
                    temp = Interval(b.start,min(a.end,b.end))
                    r.append(temp)
                    
                    
                elif check(b,a):
                    #check if a's start is in between
                    
                    temp = Interval(a.start,min(a.end,b.end))
                    r.append(temp)
                    

                
                if a.start == b.start and a.end == b.end:
                    i+=1
                    j+=1
                
                
                elif a.start >= b.start:
                    #a completely inside b
                    if a.end <= b.end:
                        i+=1
                    elif a.end > b.end:
                        #a partially inside b
                        j+=1
                        
                
                elif b.start >= a.start:
                    #b completely inside a
                    if b.end <= a.end:
                        j+=1
                    elif b.end > a.end:
                        #b partially inside a
                        i+=1
        
            else:
                break
        
        return r
