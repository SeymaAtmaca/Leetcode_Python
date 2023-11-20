class Solution:
    @cache
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ret = []
        current_prefix = 0

        for i in range(len(word)):
            current_prefix = (current_prefix * 10 + int(word[i])) % m
            ret.append(1 if current_prefix == 0 else 0)

        return ret
