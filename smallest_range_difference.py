class Solution:
	def smallestRangeI(self, A, K):
		smallest = min(A)       # smallest value
		biggest = max(A)        # biggest value
		difference = abs(biggest - smallest)        # absolute value of difference

		return 0 if difference <= 2*K else difference - 2*K
