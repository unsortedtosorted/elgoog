class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        seen=set()
        
        result =[]
        def checkSeen(r,c,seen):
            
            if (r,c) in seen:
                return True
            else:
                seen.add((r,c))
            
            return False

        def increasecol(row,col):
            
            while col<len(matrix[row]):
                if not checkSeen(row,col,seen):
                    
                    result.append(matrix[row][col])
                    col+=1
                    
                else:
                    break
            return col-1
        
        def increaserow(row,col):
            
            while row+1<len(matrix) :
                if not checkSeen(row+1,col,seen):
                   
                    result.append(matrix[row+1][col])
                    row+=1
                    
                else:
                    break

            return row
        
        def decreasecol(row,col):
            while col-1>=0:
                if not checkSeen(row,col-1,seen):
                    
                    result.append(matrix[row][col-1])
                    col-=1
                    
                else:
                    break

        def decreaserow(row,col): 
            while row-1>=0 :
                    if not checkSeen(row-1,col,seen):
                        result.append(matrix[row-1][col])
                        row-=1
                    else:
                        
                        break

        row=0
        col=0
        
        
        while  row <len(matrix) and col<len(matrix[row]):
            

            c = increasecol(row,col)
            r = increaserow(row,c)
            decreasecol(r,c)
            decreaserow(r,col)
            
            row+=1
            col+=1    
        return (result)
            
