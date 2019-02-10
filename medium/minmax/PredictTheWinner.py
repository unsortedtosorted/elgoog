"""
486. Predict the Winner

minimixe or maximize based on turn variables

each step has 2 options:
  a = start + winner(start+1,stop,-turn)
  b = stop + winner(start,stop-1,-turn)
  
  if turn==1:
    return max(a,b)
   else:
    return min(a,b)


"""



class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        
        
        def minmax(start,stop,turn):
            
            

            
            if start==stop:
                temp =  turn*nums[start]
                
                return temp
            
            else:
                
                a = turn*nums[start] + minmax(start+1,stop,-turn)
                b = turn*nums[stop]  + minmax(start,stop-1,-turn)
                
                if turn == 1:
                    return max(a,b)
                else:
                    return min(a,b)
                
        return (minmax(0,len(nums)-1,1))>=0
