"""
789. Escape The Ghosts

Find the taxicab distance between 0,0 and taget
also find taxicab distance betwee, target and all ghosts

taxicab distance = abs(x1-x2)+ abs(y1-y2)


"""


class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        
        def getTaxicabDist(src, target):
            
            return abs(src[0]-target[0])+abs(src[1]-target[1])
        
        
        pc =  getTaxicabDist([0,0], target)
        
        for x in ghosts:
            
            temp =  getTaxicabDist(x, target)
            if temp<=pc:
                return False
        
        return True
