class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()  
        visited.add(0)
        stack = [0]
        
        while stack:
            room = stack.pop() 

            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key) 

        return len(visited) == len(rooms)
