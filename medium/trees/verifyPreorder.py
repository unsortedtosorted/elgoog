"""

255. Verify Preorder Sequence in Binary Search Tree

steps:
  1. if curr is greater than low: return False
  2. while curr is greater than stack[-1],means we are in right subtree and we need to get this subtrees root, 
     which is new low value
          low = st.pop()
  3. add value to stack
  4. return False
  
RunTime : O(N)
space : O(N)


"""


class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        
        ind = 0
        st = []
        low = -sys.maxsize-1
        
        while ind < len(preorder):
            
            curr = preorder[ind]
            
            if curr < low :
                return False
            
            while len(st) > 0 and curr > st[-1]:
                low = st.pop()
                    
            st.append(curr)
            ind+=1
        

        return True
