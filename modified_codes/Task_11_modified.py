"""
Task 11 – Modified real-world case
Find the interest rate that makes two investment options equivalent
(i.e. their NPVs are equal → difference = 0).
"""
from scipy.optimize import root_scalar

# Option A cash flows
cf_A = [-8000, 2500, 3000, 3500, 2000]
# Option B cash flows
cf_B = [-10000, 3200, 3200, 3200, 3200]

# Calculate the difference between the investments' discounted cash-flow totals.
def npv_diff(r):
    npv_A = sum(cf / (1+r)**t for t, cf in enumerate(cf_A))
    npv_B = sum(cf / (1+r)**t for t, cf in enumerate(cf_B))
    return npv_A - npv_B

# Find the interest rate in the bracket where the two net present values are equal.
sol = root_scalar(npv_diff, bracket=[0.01, 0.5], method="brentq")
# Report the indifference rate and verify the NPV difference is approximately zero.
print(f"Indifference interest rate: {sol.root:.4%}")
print(f"NPV difference at that rate: {npv_diff(sol.root):.2e}")
