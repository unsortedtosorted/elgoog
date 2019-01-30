"""

157. Read N Characters Given Read4

1. Given N chars to read from a file using read4
2. Keep reading , until no characters left in the file
3. keep adding number of characters read to a varialble
4. copy read characters from buffer2 to buffer 1
5. as you copy characters to buffer1, keep reducint 1 from n
6. if n==0 , return counter
7. keep pointer p, to keep track of last place where character was written in result buffer








The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        
        buf2 = [' '] * 4
        temp = sys.maxsize
        k=0
        p = 0
        
        while temp>0 :
            
            temp = read4(buf2)
            
            for x in buf2[:temp]:
                if n==0 or x==' ':
                    return k
                buf[p]=x
                p+=1
                n-=1
                k+=1
                
                
            buf2=[' '] * 4
           
        return k
