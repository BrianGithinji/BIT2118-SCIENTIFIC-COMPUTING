"""
Task 19 – Modified real-world case
Minimise daily food cost subject to minimum protein and calorie requirements.
"""
import numpy as np
from scipy.optimize import minimize

# Variables: x = kg of food A, y = kg of food B
# Cost: 3x + 5y
# Protein: 20x + 10y ≥ 50
# Calories: 100x + 200y ≥ 400

def cost(z):
    # Return the combined cost for the proposed kilograms of both foods.
    return 3*z[0] + 5*z[1]

# Express protein and calorie minimums as nonnegative constraint functions.
cons = [
    {"type": "ineq", "fun": lambda z: 20*z[0] + 10*z[1] - 50},
    {"type": "ineq", "fun": lambda z: 100*z[0] + 200*z[1] - 400}
]

bounds = [(0, None), (0, None)]
# Find nonnegative food amounts that minimize cost while satisfying both requirements.
res = minimize(cost, [1, 1], method="SLSQP", bounds=bounds, constraints=cons)

# Display the optimizer status, selected quantities, and corresponding total cost.
print("Success:", res.success)
print(f"Food A: {res.x[0]:.3f} kg")
print(f"Food B: {res.x[1]:.3f} kg")
print(f"Minimum cost: {res.fun:.2f}")
