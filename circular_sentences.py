class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        # solution 1 ******
        # str = sentence.split()
        # if str[0][0] != str[-1][-1] : return False
        # for i in range(len(str)):
        #     if i == len(str) - 1 : 
        #         return str[i][-1] == str[0][0] 
        #     if str[i][-1] != str[i+1][0] : return False
            
        # return True


        # solution 2 ****
        str = sentence.split()
        return all(str[i][-1] == str[i+1][0] for i in range(len(str)-1)) and str[-1][-1] == str[0][0]