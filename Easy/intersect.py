"""
#350

Using HashMap:
  1. Record the occurence of each letter in first array 
  2. Iterate second array , if letter present in both, add it to result in subtract occurence from the map
  
  Space complexity is O(N), time complexity : O(N)
 
Using Sorting
  1. Sort array 1
  2. Sort array 2
  3. Now use basic of two finger algorith
  4. if number pointed to by both pointer are same, add to the array
  5. if number of pointer 1 id greater than pointer of number 2, increment number 2 and check again
  
  Time complexity : O(NLognN + MLognM + Oc) == O(NLognN), space= O(1)


"""



class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        
        m={}
        r=[]
        
        
        for x in nums1:
            
            if x in m:
                m[x]+=1
            else:
                m[x]=1
        
        for x in nums2:
            
            if x in m:
                if m[x]>0:
                    r.append(x)
                    m[x]-=1
        
        return r
