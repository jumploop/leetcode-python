class Solution:
	def largestPerimeter(self, A) -> int:
		A.sort()        # sort from the smallest to the biggest
		return next(
		    (A[i - 2] + A[i - 1] + A[i]
		     for i in range(len(A) - 1, 1, -1) if A[i - 2] + A[i - 1] > A[i]),
		    0,
		)