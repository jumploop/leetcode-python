class Solution:
	def countPrimeSetBits(self, L: int, R: int) -> int:
		def is_prime(n):
			return all(n % i != 0 for i in range(2, n)) if n > 1 else False

		count = 0
		for j in range(L, R + 1):       # R is inclusive so it has to be + 1
			n_ones = len([1 for bit in list(bin(j))[2:] if bit == '1'])     # list comprehension creates a list of ones and checks its length
			if is_prime(n_ones):
				count += 1      # add 1 if the number is prime

		return count