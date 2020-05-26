class Solution:
    def reverseVowels(self, s: str) -> str: # function name should be lower case , leetcode doesn't follow the convention
        c = list(s)  # string to list
        j = len(s) - 1
        i = 0
        vowel = ["a", "e", "i", "o", "u", 'A', 'E', 'I', 'O', 'U']

        while (i < j):
            if c[i] in vowel and c[j] in vowel:
                c[i], c[j] = c[j], c[i]  # tuple swap
                j = j - 1
                i = i + 1
            elif c[i] in vowel:
                j = j - 1
            elif c[j] in vowel:
                i = i + 1
            else:
                j = j - 1
                i = i + 1

        return ''.join(c)