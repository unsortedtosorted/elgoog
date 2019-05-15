

function travel --> 
1. Mark cell as visitedd by changing it to empty string : ""
2. if char at left is child of curr node, travel it
3. if char at right is child of curr node, travel it
4. if char at up is child of curr node, travel it
5. if char at down is child of curr node, travel it
6. if curr node is a word, add it to output
7. change current cell back to original character

pruning done via steps 2 to 5, visit next cell only if character there is a child of current of cell.

```
class Trie(object):
    
    def __init__ (self):
        self.char = None
        self.child = {}
        self.isword = False
        self.word = None


class Solution(object):
    def findWords(self, A, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
       
        words = set(words)
        out = set()
        
        head = Trie()
        
        
        def createTrie(wrd):
            curr = head
            
            for x in wrd:
                if x in curr.child:
                    curr = curr.child[x]
                else:
                    temp = Trie()
                    temp.char = x
                    curr.child[x] = temp
                    curr = temp
            curr.isword = True
            curr.word = wrd
        
        
        for x in words:
            createTrie(x)
        
        def getWords(curr):
            
            if curr:
                if curr.isword:
                    print (curr.word)
            
            for x in curr.child:
                getWords(curr.child[x])
        
                
        getWords(head)
                
        def travel(i,j,curr):
            
            
            
            
            if A[i][j] == "":
                return
            
            temp = A[i][j]
            A[i][j] = ""
            
            
            if curr.isword:
                out.add(curr.word)
            
            if i-1 >=0:
                if A[i-1][j] in curr.child:
                    travel(i-1,j,curr.child[A[i-1][j]])


            #travel south
            if i+1 < len(A):
                if A[i+1][j] in curr.child:
                    travel(i+1,j,curr.child[A[i+1][j]])

            
            #travel west
            if j-1 >=0:
                if A[i][j-1] in curr.child:
                    travel(i,j-1,curr.child[A[i][j-1]])
                
            
            #travel east
            if j+1 < len(A[i]):
                if A[i][j+1] in curr.child:
                    travel(i,j+1,curr.child[A[i][j+1]])
                
            
            A[i][j] = temp
            
        for i in range(0, len(A)):
            for j in range(0,len(A[0])):
                
                if A[i][j] in head.child:
                    
                    travel(i,j,head.child[A[i][j]])
                
                
       
        return list(out)
```
