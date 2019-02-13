"""

357. Count Numbers with Unique Digits

Create all number with repeating characters, delete them from 10**n


"""



class Solution(object):

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        self.counter = 0
        
        def backtrack(arr):
            
            if  0 not in arr and len(set(arr)) != len(arr):
                self.counter+=1
            
            count = 0
            
            if len(arr)>=n:
                return
            
            while count < 10:
                if len(arr)<1 and count == 0:
                    count+=1
                    continue
                arr.append(str(count))
                backtrack(arr)
                arr.pop()
                count+=1
        
        backtrack([])

        
        return 10**n - (self.counter)
            
