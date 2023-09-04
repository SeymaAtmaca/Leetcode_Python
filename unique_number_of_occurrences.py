class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counts = {}
        
        for num in arr:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        unique_counts = set(counts.values())
        
        return len(unique_counts) == len(counts)
