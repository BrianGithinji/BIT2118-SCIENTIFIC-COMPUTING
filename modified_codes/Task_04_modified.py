"""
Task 4 – Modified real-world case
Simple compound-interest calculation that accumulates floating-point error.
Compare naïve repeated multiplication with a more stable formulation.
"""
import numpy as np

principal = 10000.0
rate      = 0.0001          # 0.01 % per period
periods   = 1_000_000

# Repeatedly compound the balance once per period to demonstrate accumulated rounding.
balance_naive = principal
for _ in range(periods):
    balance_naive *= (1 + rate)

# Compute the mathematically equivalent balance directly with exponentiation.
balance_stable = principal * (1 + rate)**periods

# Compare the two results using absolute and relative differences.
print(f"Naïve final balance : {balance_naive:.6f}")
print(f"Stable final balance: {balance_stable:.6f}")
print(f"Absolute difference : {abs(balance_naive - balance_stable):.6e}")
print(f"Relative difference : {abs(balance_naive - balance_stable)/balance_stable:.6%}")
