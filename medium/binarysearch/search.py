"""
#702. Search in a sorted array of unknown size


"""


class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        
        start = 0
        stop  = 2147483647

        while start<=stop:
            
            mid = (start+stop)//2
            
            if reader.get(mid) == 2147483647:
                stop = mid-1
                continue
            
            elif reader.get(mid)<target:
                start=mid+1
            elif reader.get(mid)==target:
                return mid
            elif reader.get(mid)>target:
                stop=mid-1

        return -1
