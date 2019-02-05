"""
769. Max Chunks To Make Sorted

2 algo's:
 
 Slower:
 
  1. Divide the array into 2 halves:
    -- first half  : arr[:i+1]
    -- second half : arr[i+1:]
    
  2. If max of first half is less than the min of the second half, then we have found a chunk
      else continue to expand first chunk
      
   Run time : O(N){for making halves} + O(N) to find min and max 
              O(N^2)
  
  Fasteer :
  
  1. Find the max element seen until index i
  2. if max element is equal to i, then we have found a chunk
  3. e.g if arr is [0,1,2,3,4]
          0 will be at index 0
          1 will be at index 1
          2 will be at index 2
          3 will be at index 3
          4 will be at index 4
     similarly,
     if arr is [1,0,3,2,4]
     
     chunks are : [1,0] [2,3] [4]
     
     Runtime : O(N)

"""

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        def bruteForce():
            count = 0
            ma = 0
            
            for i,x in enumerate(arr):
                
                ma = max(x,ma)
                
                if ma == i :
                    count+=1
                
            return count

        return bruteForce()
                

        def Onsquare():
            r = []
            i = 0
        
            count = 0
        
            while i<len(arr):
                f = arr[:i+1]
                s = arr[i+1:]
            
                #max of first chunk should be less than
                #min of second chunk
                if len(s)==0 or max(f)<min(s)  :
                    count+=1
                
                i+=1
        
            return count
