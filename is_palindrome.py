class Solution:
    def isPalindrome(self, x: int) -> bool:

        number = str(x)     # To be able to use indices number type has to be iterable - e.g string

        return number == number[::-1]

"""
I hope I helped you in some way. If you like this solution, I'll be very happy if you click "Star" on Github:
https://github.com/JBielan/leetcode-python

Remember to have fun in coding journey. Thank you!
"""