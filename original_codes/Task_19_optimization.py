import numpy as np
from scipy.optimize import minimize

# x = number/capacity units of Type A server
# y = number/capacity units of Type B server
#
# Cost per unit: A = 12, B = 18
# Capacity per unit: A = 100, B = 170
# Required total capacity: at least 1000

def cost(z):
    # Return the total cost for the proposed amounts of Type A and Type B capacity.
    x, y = z
    return 12*x + 18*y

def capacity_constraint(z):
    # Return capacity above the minimum; a nonnegative value satisfies the constraint.
    x, y = z
    return 100*x + 170*y - 1000

# Express the minimum-capacity condition in the format expected by SLSQP.
constraints = {
    "type": "ineq",
    "fun": capacity_constraint
}

bounds = [(0, None), (0, None)]

# Find continuous nonnegative allocations that minimize cost while meeting capacity.
solution = minimize(
    cost,
    x0=[5, 3],
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

x, y = solution.x

print("Optimization success:", solution.success)
print(f"Type A allocation: {x:.3f}")
print(f"Type B allocation: {y:.3f}")
print(f"Total capacity: {100*x + 170*y:.2f}")
print(f"Minimum planning cost: {solution.fun:.2f}")

# Search integer allocations from 0 to 19 of each type and retain the least-cost feasible pair.
best_integer = None

for a in range(0, 20):
    for b in range(0, 20):
        capacity = 100*a + 170*b
        if capacity >= 1000:
            total_cost = 12*a + 18*b
            if best_integer is None or total_cost < best_integer[0]:
                best_integer = (total_cost, a, b, capacity)

print("Best nearby integer solution:", best_integer)
