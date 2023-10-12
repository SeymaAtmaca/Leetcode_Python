class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        if n == 1 and citations[0] > 0 : return 1
        if citations[-1] >= n : return n
        for i in range(n):
            if citations[i] < i+1 : return i
        return 0