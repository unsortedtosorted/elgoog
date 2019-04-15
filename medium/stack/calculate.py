"""

1. convert postfix to infix

    -- create 2 stacks:
        operators
        expression
    -- if numberix, append tot he expression
    -- if operator:
        -- if top of operator stack has priority >= empty stack into expression
        -- append it to operator
    -- in the end push last number and operator to the stack

2. Evalatuate post fix:
   -- create a new stack total
   -- iterate over the expression stack
   -- if number push if to total
   -- if an operator has come:
        rightNum = pop from total
        leftNum  = pop from total
        
        push leftNum operation rightNum to total 
3. return total[0]
        
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        oper = []
        exp = []
        
        p = {}
        p['/'] = 2
        p['*'] = 2
        p['+'] = 1
        p['-'] = 1
        
        
        #create postfix expression
        temp = ''
        
        for x in s:
            if x ==' ':
                continue
            if x.isnumeric():
                temp = temp+x
            else:
                exp.append(temp)
                temp = ''
                
                while len(oper) >0 and p[oper[-1]] >= p[x]:
                    exp.append(oper.pop())
                
                oper.append(x)
        
        exp.append(temp)
        while len(oper) > 0:
            exp.append(oper.pop())
        
        total = []
        
        
        for x in exp:
            
            if x not in p:
                total.append(int(x))
            else:
                
                r = total.pop()
                l = total.pop()
                
                result = 0
                
                if x == '+':
                    result = l+r
                elif x == '-':
                    result = l-r
                elif x == '*':
                    result = l*r
                elif x == "/":
                    result = l//r
                
                total.append(result)
        
        return total[0]
 
