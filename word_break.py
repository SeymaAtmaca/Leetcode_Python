class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # ilk i degerine göre kelimeyi ele alıyor. i den önceki kısımlar için 0-i arası hareket eden bir 
        # for dongusu pointer degiskeni ile kelimenin sözlükte olup olmadığına bakıyor.
        # burada sözlükteki kelimelerin sırası onemli.

        flag = [True]
        for i in range(1, len(s) + 1):
            flag += any(flag[j] and s[j:i] in wordDict for j in range(i)),
        
        return flag[-1]