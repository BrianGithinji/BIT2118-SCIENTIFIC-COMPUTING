"""
Task 12 – Modified real-world case
Find intersection of a robot’s straight-line path and a circular obstacle.
Line:   y = 0.5 x
Circle: (x-2)² + (y-1)² = 1
"""
import numpy as np
from scipy.optimize import root

def equations(z):
    # Return line and circle residuals; an intersection makes both values zero.
    x, y = z
    return [
        y - 0.5*x,                     # line
        (x-2)**2 + (y-1)**2 - 1        # circle
    ]

# Use starting estimates near the two expected intersections to locate both solutions.
for guess in ([1.0, 0.5], [3.0, 1.5]):
    sol = root(equations, guess)
    print("Guess:", guess)
    print("  Intersection:", np.round(sol.x, 4))
    print("  Residuals   :", np.round(equations(sol.x), 8))
    print("  Converged   :", sol.success)
    print()
