import numpy as np

# Show that decimal fractions can be inexact in binary floating-point representation.
calculated = 0.1 + 0.2
expected = 0.3

# Compare direct equality with NumPy's tolerance-based floating-point comparison.
print("0.1 + 0.2 =", calculated)
print("Exact comparison:", calculated == expected)
print("Tolerance-based comparison:", np.isclose(calculated, expected))

# Compare an approximation to the high-precision square root of 2.
true_value = np.sqrt(2)
approx_value = 1.414

absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)

print(f"Absolute error: {absolute_error:.8f}")
print(f"Relative error: {relative_error:.8%}")

# Compare two equivalent formulas; the second avoids subtracting nearly equal values.
for x in [1e-4, 1e-8, 1e-12]:
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)
    # Print both results to show how round-off affects the direct expression for small x.
    print(f"x={x:.0e}: direct={direct:.12f}, stable={stable:.12f}")
