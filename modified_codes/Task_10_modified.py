"""
Task 10 – Modified real-world case
Break-even analysis: find the production quantity Q where
Revenue = Cost  →  40Q = 5000 + 25Q
"""
import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

def profit(Q):
    # Return revenue minus total cost; break-even occurs where this value is zero.
    return 40*Q - (5000 + 25*Q)   # Revenue - Cost

# Find the zero of the profit function within the specified quantity interval.
sol = root_scalar(profit, bracket=[0, 1000], method="bisect")
print(f"Break-even quantity: {sol.root:.1f} units")

# Generate quantities for plotting revenue and cost around the break-even point.
Q = np.linspace(0, 600, 300)
plt.plot(Q, 40*Q, label="Revenue")
plt.plot(Q, 5000 + 25*Q, label="Total Cost")
plt.axvline(sol.root, linestyle="--", color="k", label="Break-even")
plt.xlabel("Quantity")
plt.ylabel("Money")
plt.title("Break-even analysis")
plt.legend()
plt.grid(True)
plt.savefig("Task_10_modified_breakeven.png")
plt.show()
