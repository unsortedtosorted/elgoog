"""
#unionfind solution also possible

737. Sentence Similarity II

1. create a graph of words
2. check if 2 words are similar by traversing graph

"""


class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        
        if len(words1) != len(words2):
            return False
        graph = collections.defaultdict(list)
        
        def createGraph():
            
            for x in pairs:
                
                graph[x[0]].append(x[1])
                graph[x[1]].append(x[0])
        createGraph()      
        
        
        def checkword(w1,w2):
            
            toVisit = [w1]
            seen = set()
            
            while len(toVisit) > 0:
                
                curr = toVisit.pop()
                if curr in seen:
                    continue
                seen.add(curr)
                for x in graph[curr]:
                    
                    if x == w2:
                        return True
                        
                    toVisit.append(x)

            return False
        
        
        for i,x in enumerate(words1):

            if x != words2[i]:
                if not checkword(x,words2[i]):
                    return False
        
        return True
