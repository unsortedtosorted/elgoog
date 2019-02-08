"""
398. Random Pick Index

Reservoir sampling

When we have n item, probability of picking 1 item is 1/n.
But if we have limited space , example k, and inifite length data, then we use reservoir sampling

Algo.
  1. let count = 0
  2. let memory = 1
  3. if index i, is target :
    3.1 result is i if 1/random.number(1,count) is == 1, we replace
    other wise continue
    
    Run Time : O(N)
    space : O(1)
  

"""



class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.m = nums
        
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        
        memory = 0
        idx = 0
        
        for i,x in enumerate(self.m):
            
            if x == target:
                #increase memory by 1
                memory+=1          
                temp = 1/random.randint(1,memory)
                
                if temp == 1:
     
                    idx = i
        return idx
        
