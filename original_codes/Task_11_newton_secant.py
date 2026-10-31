from scipy.optimize import root_scalar

# Initial investment followed by annual cash inflows
cash_flows = [-10000, 3000, 3500, 4000, 2500]

# Compute net present value by discounting each year's cash flow at the given rate.
def npv(rate):
    return sum(
        cf / (1 + rate)**t
        for t, cf in enumerate(cash_flows)
    )

# Compute the derivative of NPV with respect to the discount rate for Newton's method.
def d_npv(rate):
    return sum(
        -t * cf / (1 + rate)**(t + 1)
        for t, cf in enumerate(cash_flows)
        if t > 0
    )

# Find the rate that makes NPV zero using Newton's method and its derivative.
newton = root_scalar(
    npv,
    fprime=d_npv,
    x0=0.10,
    method="newton",
    xtol=1e-12
)

# Find the same zero with the Secant method, which estimates the derivative numerically.
secant = root_scalar(
    npv,
    x0=0.05,
    x1=0.20,
    method="secant",
    xtol=1e-12
)

# Report both estimated internal rates of return and check NPV at Newton's result.
print(f"IRR using Newton-Raphson: {newton.root:.6%}")
print(f"IRR using Secant method:  {secant.root:.6%}")
print(f"NPV at Newton solution:   {npv(newton.root):.6f}")
