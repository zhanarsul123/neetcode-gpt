class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        if iterations == 0:
            return init
        x = float(init)
        for _ in range(iterations):
            gradient = 2 * x
            x = x - learning_rate * gradient
        return round(x, 5)


sol = Solution()
print(sol.get_minimizer(0, 0.01, 5))
print(sol.get_minimizer(10, 0.01, 5))




       
        # Round final answer to 5 decimal places
pass
