"""

609. Find Duplicate File in System

1. use hashmap with kay as content and value as list of filepaths
2. for every key if lenght of list is greater than 1, add it to result

Runtime : 

"""


class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        
        
        content = {}
        
        for x in paths:
            
            l = x.split(" ")
            direc = l[0]
            
            for x in l[1:]:
                
                s = x.split(".txt")
                fname = s[0]
                fc = s[1]
                
                if fc in content:
                    content[fc].append(direc+"/"+fname+".txt")
                else:
                    content[fc] = [(direc+"/"+fname+".txt")]
        
        r =[]

        
        for x in content:
            if len(content[x]) > 1:
                r.append(content[x])
        
        return r
