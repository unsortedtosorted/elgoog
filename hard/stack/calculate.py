class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        num=""
        sign = 1
        result = 0
        
        stack = []
        
        for x in s:
            
            if x.isdigit():
                num = num+x
            
            elif x == "+":
                result = result+ sign*int(num)
                num=""
                sign = 1
            
            elif x == "-":
                result = result +sign*int(num)
                num=""
                sign = -1
                
               
            
            elif x == "(":
               
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
                num =""
                
            
            elif x == ")":
               
                result=result+sign*int(num)
                
                sign=stack.pop()
                temp =stack.pop()
                result = result*sign+temp
                num="0"
                sign=1
                
        
            
        
        return result+sign*int(num)
                
