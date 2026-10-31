import numpy as np
from scipy.linalg import lu_factor, lu_solve

# The same coefficient matrix is reused for several measurement vectors.
A = np.array([
    [4.0, -1.0,  0.0],
    [-1.0, 4.0, -1.0],
    [0.0, -1.0,  3.0]
])

measurement_sets = [
    np.array([15.0, 10.0, 10.0]),
    np.array([16.0, 11.0,  9.0]),
    np.array([14.0, 12.0, 11.0])
]

# Factor A once so its LU decomposition can be reused for each right-hand side.
lu, piv = lu_factor(A)

# Solve the system for each measurement vector and report its residual size.
for i, b in enumerate(measurement_sets, start=1):
    x = lu_solve((lu, piv), b)
    residual = b - A @ x
    print(f"Measurement set {i}")
    print("Solution:", x)
    print("Residual norm:", np.linalg.norm(residual))
    print()

# Compare the first LU-based result with NumPy's direct linear solver.
print("Direct solution for first set:",
      np.linalg.solve(A, measurement_sets[0]))
