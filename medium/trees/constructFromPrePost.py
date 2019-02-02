"""
889. Construct Binary Tree from Preorder and Postorder 

1. Start with first element in preorder
2. Search for index,j of same number in postorder
3. left child = i+1
4. right child = j+1
5. if left child is not equal to right child and both already not marked, create tree.left and tree.right
6. if left child is equal to right child and both not marked, create tree.left

Run Time : O(N^2)


"""



class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        
        pre : ro l r
        post : l r ro
        
        """
        
        
        def search(val):
            
            for i,x in enumerate(post):
                if x==val:
                    return i

        parent = {}        
        i = 0
        
        
        root = TreeNode(pre[i])
        temp = root
        parent[pre[i]]=root
        
        while i<len(pre):
            
            temp = parent[pre[i]]
            j = search(pre[i])
            
            #get l from pre
            if i+1<len(pre):
                lpre = pre[i+1]
            else:
                lpre = pre[i]
            
            
            #get r from post
            if j-1>-1:
                rpost = post[j-1]
            else:
                rpost = post[j]
            

            if lpre==rpost:
                if lpre not in parent:
                    temp.left = TreeNode(lpre)
                    parent[lpre]=temp.left
            else:
                if (lpre not in parent) and ( rpost not in parent):
                    
                    temp.left = TreeNode(lpre)
                    temp.right = TreeNode(rpost)
                    parent[lpre] = temp.left
                    parent[rpost]= temp.right
            
            i+=1
            j-=1
        
        
        return root
