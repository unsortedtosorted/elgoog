class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        
        if len(words1)!=len(words2):
            return False
        
        
        m = {}
        
        for x in pairs:
            
            w1 = x[0]
            w2 = x[1]
            
            if w1 in m:
                m[w1].append(w2)
            else:
                m[w1]=[w2]
            
            if w2 in m:
                m[w2].append(w1)
            else:
                m[w2]=[w1]
            
            
        
        for i,x in enumerate(words1):
            
            w2=words2[i]
            if x==w2:
                continue
            else:
                if (x in m and w2 in m[x]) or (w2 in m and x in m[w2]):
                    continue
                else:
                    return False
        
        
        
        return True
            
            
