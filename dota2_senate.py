class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        senate = list(senate)
        n = len(senate)
        D,R = deque(), deque()
        for i in range(n):
            if senate[i] == "R": R.append(i)
            else : D.append(i)
        
        while D and R : 
            dpop, rpop = D.popleft(), R.popleft()
            if dpop < rpop : 
                D.append(dpop + n)
            else : 
                R.append(rpop + n)
        
        if not D : 
            return "Radiant"
        else : 
            return "Dire"
        