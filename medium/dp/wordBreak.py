class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        self.d=set()
        self.memo={}
        
        for x in wordDict:
            self.d.add(x)
            
        
        def checkWord(word):
            
            if word in self.memo:
                return self.memo[word]
            
 
            temp = ""
            
            if word in self.d:
                self.memo[word]=True
                return True
            
            
            for i,x in enumerate(word):
                
                temp=temp+x
                if temp in  self.d:
                    if checkWord(word[i+1:]):
                        self.memo[word]=True
                        return True
            
            self.memo[word]=False
            return False
        return checkWord(s)
                    
