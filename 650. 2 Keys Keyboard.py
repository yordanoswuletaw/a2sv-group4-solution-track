class Solution:
    def minSteps(self, n: int) -> int:
        factors = []
        for i in range(2, n + 1):
            while n % i == 0:
                factors.append(i)
                n /= i
                
        return sum(factors)
