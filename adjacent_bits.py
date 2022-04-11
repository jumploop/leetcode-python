class Solution:
	def hasAlternatingBits(self, n: int) -> bool:
		binary = bin(n)     # string representation of binary number like 0b10 is 2
		return all(binary[i] != binary[i + 1] for i in range(2, len(binary ) - 1))
