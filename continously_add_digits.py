class Solution:
	def addDigits(self, num: int) -> int:
		while num >= 10:        # as long as there's 2 digits number
			num = str(num)      # turn num into string to be able to iterate through digits
			temp = sum(int(digit) for digit in num)
			num = temp      # set new num

		return num      # return num when while loop break