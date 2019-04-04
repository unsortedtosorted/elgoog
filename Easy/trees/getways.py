"""

437. Path Sum III

If we have to find number of ways only from root, then solution is easy.
Only difference here is we have to call our code for each node , considering it as new root.

Getways(root,remain) return numbder of ways to reach sum from root node
do any tree traversal (pre/post/in) and call getways for each node.

"""


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
    
        
        def getways(root,remain):
            
            numWays = 0
            if root:
                
                if root.val == remain:
                    numWays+=1
                return numWays+getways(root.left,remain-root.val)+getways(root.right,remain-root.val)

            else:
                return numWays
            
        def traverse(root):
            
            ways = 0
            if root:
                
                ways += getways(root,sum) + traverse(root.left) + traverse(root.right)
            return ways
        return traverse(root)
