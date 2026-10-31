import numpy as np

# x = number of Type A servers
# y = number of Type B servers
#
# Type A uses 4 CPU units and 8 GB memory
# Type B uses 2 CPU units and 12 GB memory
# Total observed usage: 20 CPU units and 72 GB memory

# Put CPU and memory usage coefficients in rows and server types in columns.
A = np.array([
    [4.0,  2.0],
    [8.0, 12.0]
])

# Store the observed totals for CPU units and memory in the same row order as A.
b = np.array([20.0, 72.0])

# Solve A @ solution = b to estimate the numbers of each server type.
solution = np.linalg.solve(A, b)
# Calculate the difference between observed and reconstructed resource totals.
residual = b - A @ solution

# Print the estimates and check that they reproduce the input totals accurately.
print(f"Type A servers: {solution[0]:.0f}")
print(f"Type B servers: {solution[1]:.0f}")
print("Verification A @ solution:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))
