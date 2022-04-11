class Solution:
	def distributeCandies(self, candies) -> int:
		n_candies = len(candies)        # number of candies
		n_kinds = len(set(candies))     # number of kinds

		return n_candies // 2 if n_kinds > n_candies / 2 else n_kinds
