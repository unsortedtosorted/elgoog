"""

1 = 2
10 = 2*1+0 = 2
101 = 2*2+1 = 5
1011 = 2*5 +1 =11

"""


class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        curr = 0
        r = []
        for i,x in enumerate(A):
            
            curr = curr*2 + x
            r.append(curr%5==0)

        return r
