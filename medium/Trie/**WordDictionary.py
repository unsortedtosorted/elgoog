from collections import deque
class tNode(object):
    def __init__(self,x):
        self.val = x
        self.child = {}
        self.isWord = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=tNode(None)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        temp=self.root
        for x in word:
            if x in temp.child:
                temp=temp.child[x]
            else:
                temp.child[x]=tNode(x)
                temp=temp.child[x]
        
        temp.isWord=True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        
        temp = self.root

        def srchfrom(word,root):
            
            for i,x in enumerate(word):        
                if x=='.':
                    for y in root.child:
                        if srchfrom(word[i+1:],root.child[y]):
                            return True
                    return False
                    
                else:
                    if x in root.child:
                        root=root.child[x]
                    else:
                        return False
       
            return root.isWord
        return srchfrom(word,temp)
