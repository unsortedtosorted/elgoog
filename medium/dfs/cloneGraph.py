"""

To copy a node we need 2 things:
1. value : can be copied directly
2. neighbors : little tricky

To add neighbors to a copyNode we need to make sure copy of those neighbors also exist

if they dont then we create them and store the reference in hashmap
if they do then retreive it from map
finally add the copy of neighbor to the neighbor list of current node
Space : O(V)
Runtime : O(E*V)

"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        #create reference for node to return
        to_return = Node(node.val,None)
        
        to_visit = [node]
        visited = set()
        
        #map to store copy of a node
        copy = {}
        copy[node] = to_return 
        
        while len(to_visit) > 0:
            
            curr = to_visit.pop()
            
            #if node is visited continue
            if curr not in visited:
                visited.add(curr)
            else:
                continue
            
            copy_node = copy[curr]
            copy_node.neighbors = [] 
            for x in curr.neighbors:
                if x in visited:
                    continue
                    
                if x not in copy:
                    copy[x] = Node(x.val,x.neighbors)
                to_visit.append(x)
            
            #Add neigh to curr
            for x in curr.neighbors:
                nei = copy[x]
                copy_node.neighbors.append(nei)
        
        
        return to_return
