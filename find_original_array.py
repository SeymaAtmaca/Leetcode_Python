class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if(len(changed) % 2 == 1) : return []

        changed.sort()
        res,queue = deque(), deque()

        for num in changed : 
            if queue and queue[0] * 2 == num : 
                res.append(queue.popleft())
            else : queue.append(num)
        
        return [] if queue else res
        