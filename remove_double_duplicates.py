class Solution:
	def removeDuplicates(self, S: str) -> str:
		i = 0
		while i < len(S) - 1:       # while is necessary to check the length after every loop
			if S[i] == S[i + 1]:
				S = S[:i] + S[i+2:]     # remove duplicates
				i -= 2 if i > 0 else 1
			i += 1      # go at the next place of the list

		return S