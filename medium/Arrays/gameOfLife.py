class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        prev = {}
        
        def updatestate(x,y,prev):
            
            live=0

            
            #check upleft
            if x-1 >=0 and y-1>=0:
                
                if (str(x-1)+","+str(y-1)) in prev:
                    if prev[str(x-1)+","+str(y-1)]==1:
                        live+=1
                else:
                    if board[x-1][y-1]==1:
                        #print("upleft")
                        live+=1
                
            
            #check downright
            if x+1<len(board) and y+1<len(board[x]):
                if (str(x+1)+","+str(y+1)) in prev:
                    if prev[str(x+1)+","+str(y+1)]==1:
                        live+=1
                else:
                    if board[x+1][y+1]==1:
                       
                        #print("upleft")
                        live+=1
                        
                
            #check up
            if x-1>=0:
                if (str(x-1)+","+str(y)) in prev:
                    if prev[str(x-1)+","+str(y)]==1:
                        live+=1
                else:
                    if board[x-1][y]==1:
                        #print("upleft")
                        live+=1
 
            
            #check down
            if x+1<len(board):
                if (str(x+1)+","+str(y)) in prev:
                    if prev[str(x+1)+","+str(y)]==1:
                        live+=1
                else:
                    if board[x+1][y]==1:
                        
                        
                        live+=1

            
            #check left
            if y-1>=0:
                if (str(x)+","+str(y-1)) in prev:
                    if prev[str(x)+","+str(y-1)]==1:
                        live+=1
                else:
                    if board[x][y-1]==1:
                        #print("upleft")
                        live+=1

            
            #check upright
            if x-1>=0 and y+1<len(board[x-1]):
                if (str(x-1)+","+str(y+1)) in prev:
                    if prev[str(x-1)+","+str(y+1)]==1:
                        live+=1
                else:
                    if board[x-1][y+1]==1:
                        #print("upleft")
                        print("down")
                        live+=1
                        
  
            #check down left
            if x+1<len(board) and y-1>=0:
                if (str(x+1)+","+str(y-1)) in prev:
                    if prev[str(x+1)+","+str(y-1)]==1:
                        live+=1
                else:
                    if board[x+1][y-1]==1:
                        #print("upleft")
                        live+=1
            
            
            #check right
            if y+1<len(board[x]):
                if (str(x)+","+str(y+1)) in prev:
                    if prev[str(x)+","+str(y+1)]==1:
                        live+=1
                else:
                    if board[x][y+1]==1:
                        #print("upleft")
                        live+=1
                        

            
            
            prev[str(x)+","+str(y)]=board[x][y]
            
            if live<2:
                board[x][y]=0
            elif live>3:
                board[x][y]=0
            elif live==3:
                board[x][y]=1
                
            
                
                
                
        
        
        
    
        for i,x in enumerate(board):
            for j,y in enumerate(x):
                updatestate(i,j,prev)
               
