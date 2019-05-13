"""
#516

The problem can be divided into 2 types of subproblems (i = start, j = end):
* if start and end char match s[i] == s[j]:
	* 	 dp(i,j) = 2 + dp(i+1, j-1 ) --> we want to keep both in out longest sequence so add 2
* else:
	* 	dp (i,j) = max(dp(i,j-1),dp(i+1,j) --> we want to change start and stop combinations and use the one that has max length
	

		

```
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        memo = {}
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i > j :
                memo[(i,j)] = 0
                return 0
            
            if i == j:
                memo[(i,j)] = 1
                return 1
            
            else:
                ma = 0
                if s[i] == s[j]:
                    memo[(i,j)] = 2 +dp(i+1,j-1)
                    return 2 +dp(i+1,j-1)
                else:
                    
                    ma = max(dp(i,j-1),dp(i+1,j))
                memo[(i,j)] = ma
                return ma
        
        return dp(0,len(s)-1)
                    
```
