"""
Task 6 – Modified real-world case
Balance the chemical equation for combustion of propane:
   a C3H8 + b O2 → c CO2 + d H2O
We obtain a linear system from atom conservation.
"""
import numpy as np

# Variables: [a, b, c, d]
# Carbon:   3a     = c
# Hydrogen: 8a     = 2d
# Oxygen:   2b     = 2c + d
# Normalise a = 1  →  four equations, four unknowns (one is free)

A = np.array([
    [3, 0, -1,  0],   # C
    [8, 0,  0, -2],   # H
    [0, 2, -2, -1],   # O
    [1, 0,  0,  0]    # set a = 1
], dtype=float)

# Set the conservation-equation right-hand sides to zero and fix propane's coefficient a to 1.
b = np.array([0, 0, 0, 1], dtype=float)

# Solve for the stoichiometric coefficients that satisfy all atom-balance equations.
sol = np.linalg.solve(A, b)
# Report the coefficients and check that they satisfy the system.
print("Stoichiometric coefficients [a, b, c, d]:")
print(np.round(sol, 4))
print("Verification residual:", np.round(A @ sol - b, 10))
