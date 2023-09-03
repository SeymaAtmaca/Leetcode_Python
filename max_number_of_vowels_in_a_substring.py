class Solution(object):
    def maxVowels(self, s, k):
        vowels = set("aeiou")
        max_vowels = 0
        current_vowels = 0

        for i in range(len(s)):
            if s[i] in vowels: current_vowels += 1
            if i >= k:
                if s[i - k] in vowels: current_vowels -= 1
            max_vowels = max(max_vowels, current_vowels)
        return max_vowels
