class tNode:
    def __init__(self, x):
        self.val = x
        self.isWord=False
        self.child = {}
        

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=tNode(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        temp=self.root
        for x in word:
            if x in temp.child:
                temp=temp.child[x]
            else:
                child=tNode(x)
                temp.child[x]=child
                temp=temp.child[x]
        temp.isWord=True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        temp=self.root
        
        for x in word:
            if x in temp.child:
                temp=temp.child[x]
                
            else:
                return False
        
        return temp.isWord
        
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        
        temp=self.root
        for x in prefix:
            if x in temp.child:
                temp=temp.child[x]
                
            else:
                return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
