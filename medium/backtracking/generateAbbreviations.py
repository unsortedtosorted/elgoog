"""
320. Generalized Abbreviation

1. Given word , generate all premutations of generalized abbreviations.

Algo:
  1. for each char in word, if char is not digit, change it to 1
  2. compress it, add to the set
  3. again generate permuations
  
  Runtime : O(n*2n)


"""


class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        self.m = {}
        def compress(word):
            
            k = "".join(word)
            if k in self.m:
                return self.m[k]
            
            temp = []
            count = 0
            for i,x in enumerate(word):
                if not x.isdigit():
                    if count:
                        temp.append(str(count))
                        count = 0
                    temp.append(x)
                else:
                    count+=int(x)
            if count:
                temp.append(str(count))
            self.m[k] = temp
            return temp
        
        output = set()
        
        def backtrack(word):
            
            for i,x in enumerate(word):
                
                if not x.isdigit():
                
                    word[i] = '1'
                    temp = compress(word)
                    tempword = "".join(temp)
                    
                    if tempword not in output:
                        
                        backtrack(temp)
                        output.add(tempword)
                    
                    word[i]=x
        
        backtrack(list(word))
        output.add(word)

        return  list(output)
