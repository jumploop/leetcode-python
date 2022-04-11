class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1

        results = [0, 1]

        results.extend(sum(results[-2:]) for _ in range(1, N))
        return results[-1]
