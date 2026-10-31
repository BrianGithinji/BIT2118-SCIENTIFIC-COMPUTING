"""
Task 8 – Modified real-world case
1-D steady heat conduction with different boundary temperatures
(left = 80 °C, right = 10 °C) solved by Gauss-Seidel.
"""
import numpy as np
import matplotlib.pyplot as plt

n = 7
# Build the tridiagonal coefficient matrix for the one-dimensional conduction model.
A = np.zeros((n, n))
for i in range(n):
    A[i, i] = 2.0
    if i > 0:
        A[i, i-1] = -1.0
    if i < n-1:
        A[i, i+1] = -1.0

# Encode the influence of the fixed left and right boundary temperatures.
b = np.zeros(n)
b[0]  = 80.0          # left boundary influence
b[-1] = 10.0          # right boundary influence

def gauss_seidel(A, b, tol=1e-10, max_iter=1000):
    # Initialize the interior temperature estimates and record iteration changes.
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        # Retain old values for components not yet updated during this iteration.
        old = x.copy()
        for i in range(len(b)):
            # Use newest values to the left and previous-iteration values to the right.
            s1 = A[i, :i] @ x[:i]
            s2 = A[i, i+1:] @ old[i+1:]
            x[i] = (b[i] - s1 - s2) / A[i, i]
        # Stop once the largest temperature change is below the requested tolerance.
        err = np.linalg.norm(x - old, np.inf)
        errors.append(err)
        if err < tol:
            break
    return x, errors

# Solve for the interior temperatures and display convergence information.
T, errs = gauss_seidel(A, b)
print("Temperatures (°C):", np.round(T, 2))
print("Iterations:", len(errs))

# Plot the largest update per iteration on a logarithmic scale.
plt.semilogy(errs)
plt.xlabel("Iteration")
plt.ylabel("Max change")
plt.title("Gauss-Seidel convergence – heat conduction")
plt.grid(True)
plt.savefig("Task_08_modified_convergence.png")
plt.show()
