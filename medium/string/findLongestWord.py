"""

524. Longest Word in Dictionary through Deleting

Algo:
  1. Check if two string can be made equal by deletiong using 2 pointers
  2. add to result if true and length equal to last string added
  3. if greater make list empty and add the element.
  4. sort the list and return 0th element
  
  Runtime:
  
  O(M*N)


"""




class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        
        
        def checkWords(word):
            
            i = 0
            j = 0
            
            while i <len(s) and j <len(word):
                
                if s[i] == word[j]:
                    
                    j+=1

                i+=1
            
            if j == len(word):
                return True
            else:
                return False
        
        r = []
        for x in d:
            
            if checkWords(x):
                if len(r)==0:
                    r = [x]
                    continue
                if len(x) > len(r[0]):
                    r = [x]
                elif len(x) == len(r[0]):
                    r.append(x)
        
        r = sorted(r)
        
        if len(r)>0:
            return r[0]
        else:
            return ""
        
