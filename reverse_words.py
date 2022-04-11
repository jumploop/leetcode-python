class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')  # creates a list of words
        reverse = [word[::-1] for word in s]
        return ' '.join(reverse)
