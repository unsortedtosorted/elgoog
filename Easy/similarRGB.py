"""
#800

1. Find the closest RGB color to given color that can be written in shorthand
2. If given number is #ABCDEF break it down into AB,CD,EF
3. Find the closest number to AB that can be written as xx
4. Find the closest number to CD that can be written as xx
5. Find the closest number to EF that can be written as xx

return output string

"""





class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        d=['00','11','22','33','44','55','66','77','88','99','aa','bb','cc','dd','ee','ff']
        
        def getHexToInt(x):
            return int(x,16)
        
        def getNearest(a):
            diff= sys.maxsize
            r='00'
            
            for x in d:
                temp = abs(getHexToInt(x)-a)
                if temp<diff:
                    diff=temp
                    r=x
            return r
                
        x=0
        o="#"
        while x+1<len(color):
            if x==0:
                x+=1
                continue
            
            a = color[x]+color[x+1]
            num = getHexToInt(a)
            y = getNearest(num)
            o = o+ y
            x+=2
        return (o)
