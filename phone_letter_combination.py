class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        data = {"2":"abc", "3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        ret = []

        def comb ( combination, next_digit):
            if not next_digit:
                ret.append(combination)
                return

            for letter in data[next_digit[0]]:
                comb(combination + letter, next_digit[1:])
            
        comb("", digits)
        return ret
                