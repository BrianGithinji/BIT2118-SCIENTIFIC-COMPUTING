import numpy as np
import matplotlib.pyplot as plt

# Simplified steady-state temperature model for five interior grid points.
# Diagonal dominance makes Jacobi and Gauss-Seidel converge.
A = np.array([
    [ 2., -1.,  0.,  0.,  0.],
    [-1.,  2., -1.,  0.,  0.],
    [ 0., -1.,  2., -1.,  0.],
    [ 0.,  0., -1.,  2., -1.],
    [ 0.,  0.,  0., -1.,  2.]
])

# Boundary influence: left boundary = 100 C, right boundary = 20 C
b = np.array([100., 0., 0., 0., 20.])

def jacobi(A, b, tol=1e-8, max_iter=500):
    # Separate the diagonal from the off-diagonal terms for the Jacobi update.
    D = np.diag(A)
    R = A - np.diagflat(D)
    # Begin with a zero estimate and save the largest change from each iteration.
    x = np.zeros_like(b)
    errors = []

    for _ in range(max_iter):
        # Compute all components from the previous iterate, then measure the change.
        x_new = (b - R @ x) / D
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x_new, errors
        x = x_new

    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    # Begin with a zero estimate; Gauss-Seidel reuses updated values within each pass.
    x = np.zeros_like(b)
    errors = []

    for _ in range(max_iter):
        # Preserve the previous iterate for components that have not yet been updated.
        old = x.copy()
        for i in range(len(b)):
            x[i] = (
                b[i]
                - A[i, :i] @ x[:i]
                - A[i, i+1:] @ old[i+1:]
            ) / A[i, i]

        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x, errors

    return x, errors

# Solve with both iterative methods and compute a direct solution as a reference.
x_j, err_j = jacobi(A, b)
x_gs, err_gs = gauss_seidel(A, b)
x_exact = np.linalg.solve(A, b)

print("Jacobi temperatures:", x_j)
print("Gauss-Seidel temperatures:", x_gs)
print("Direct solution:", x_exact)

# Plot each method's largest update per iteration on a logarithmic y-axis.
plt.semilogy(err_j, label="Jacobi")
plt.semilogy(err_gs, label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Maximum change")
plt.title("Convergence of iterative temperature solution")
plt.legend()
plt.grid(True)
plt.savefig("Task_08_convergence.png")
plt.show()
