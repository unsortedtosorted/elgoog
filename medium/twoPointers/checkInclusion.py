"""
567. Permutation in String

Steps:

create an array of length 26

for string s1, update the array e.g if a comes twice array[0] = 2

now maintain 2 pointers and do the same for string s2, and compare the list each time with s1's array

 
 
 Runtime : O (N)

"""


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if len(s1) > len(s2):
            return False
        
        l1 = [0]*26
        l2 = [0]*26
        
        for x in s1 :
            
            l1[ord(x)-ord('a')]+=1
        
        
        curr = 0
        
        while curr <len(s1)-1:
            x = s2[curr]
            l2[ord(x)-ord('a')]+=1
            curr+=1
        
        
        start = 0
        
        while curr < len(s2):
            x = s2[curr]
            l2[ord(x)-ord('a')]+=1
            if l2==l1:
                return True
            else:
                l2[ord(s2[start])-ord('a')]-=1
                
            start+=1
            curr+=1
