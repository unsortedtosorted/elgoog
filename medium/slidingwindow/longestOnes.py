"""
1004. Max Consecutive Ones III

1. Create a queue
2. if 1 , increase count by 1
3. if 0, add index of zero to q
    1. if length of q is less than equal to k, increase count by 1
    2. else, count = max(count, tempcount)
            tempcount = q[-1]-q[0]

"""



from collections import deque
class Solution(object):
    def longestOnes(self, arr, k):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        q = deque()

        count = 0
        maxo = -sys.maxsize - 1
        for i,x in enumerate(arr):

            if x == 1:
                count+=1

            if x == 0 :

                q.append(i)

                if len(q)<=k:
                    count+=1

                elif len(q)>k:
                    maxo = max(maxo,count)  
                    start = q[0]
                    stop = q[-1]
                    count =stop - start
                    q.popleft()
                    

        maxo = max(maxo, count)
        
        return maxo
