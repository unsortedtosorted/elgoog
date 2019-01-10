class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        l=[]
        
        people = sorted (people , key = lambda x: (x[0],-x[1]), reverse=True )

        for x in people:

            l.insert( x[1] , [x[0],x[1]])
        
        return (l)
