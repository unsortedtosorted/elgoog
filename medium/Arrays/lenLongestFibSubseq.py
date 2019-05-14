"""

873. Length of Longest Fibonacci Subsequence

1. for every i, check value of j for which longest chain exists 
2. example :
  
  [1,2,3,4,5,6,7,8]
  
  start with i = 0, check if 
                    A[i] + A[i+1] in array if yes : get chain lenght
                    A[i] + A[i+2] in array if yes : get chain lenght
                    
                    get(max) chain length
                  
            do it till i = len(arr)-1



"""

class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        m = {}
        
        for i,x in enumerate(A):
            
            m[x] = i
            
        
        ma = 0
        
        def checkChain(i,j):
            num1 = A[i]
            num2 = A[j]
            count = 0
            
            while True:
                s = num1+num2
                
                if s in m and m[s] > j:
                    num1 = num2
                    num2 = A[m[s]]
                    j = m[s]
                    
                    count+=1
                else:
                    break
            if count > 0:
                count +=2
            return count
        
        
        for i in range(0,len(A)-1):
            temp = 0
            
            for j in range(i+1,len(A)):
                
                num1 = A[i]
                num2 = A[j]
                
                if num1+num2 in m:
                    
                    temp = checkChain(i,j)
                    
                ma = max(ma,temp)
        
        return ma
