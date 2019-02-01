"""
647. Palindromic Substrings

1. Given a string find the number of palindromic substrings.
2. If string is length of N, then there are 2*N-1 centre
3. for each centre check if left == right , if yes, its a palindrome
4. the left and right will follow this pattern:
    00
    01
    11
    12
    22
    23
    ...
 
 Run Time: O(N^2)
 Space : O(1)

"""

class Solution(object):
    def countSubstrings(self, S):
        
        count = 0
        for i in range(0,len(S)):
            left = i
            right =i

            while left>=0 and right <len(S) and S[left]==S[right]:
                count+=1
                left-=1
                right+=1

            left=i
            right=left+1
            
            while left>=0 and right <len(S) and S[left]==S[right]:
                count+=1
                left-=1
                right+=1

        return count
