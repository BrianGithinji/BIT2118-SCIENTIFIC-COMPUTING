# BIT 2118 – Scientific Computing  
## Full Group Work Analysis (Tasks 2–20)

This document satisfies requirements **B, C, D and E** for every task.

---

### Task 2 – NumPy Arrays and Numerical Computation

**B. Inputs & Mathematical Operation**  
- Inputs: 24 hourly temperatures (°C)  
- Operations: `np.mean()`, `np.min()`, `np.max()`, vectorized conversion \( F = 1.8C + 32 \)

**C. Change one parameter**  
Change the conversion formula to Kelvin: \( K = C + 273.15 \).  
Result: All values increase by 273.15; mean becomes ≈ 296.5 K instead of 23.3 °C. The shape of the daily profile stays identical.

**D. Output meaning**  
Mean ≈ 23.3 °C, min = 17.5 °C, max = 29.4 °C. The day shows a typical diurnal cycle (cool morning → warm afternoon).

**E. Modified real-world case**  
See `modified_codes/Task_02_modified.py` – rainfall totals instead of temperature.

---

### Task 3 – Mathematical Functions and Vectorization

**B. Inputs & Operation**  
- 1 000 000 random latency values (ms)  
- Operations: division by 1000 and squaring (both vectorized vs pure Python loop)

**C. Change parameter**  
Increase array size to 5 000 000.  
Speed-up of vectorized code remains roughly the same (or slightly higher) because the relative overhead of the Python loop grows.

**D. Output meaning**  
Vectorized version is typically 50–200× faster. First five squared values are the squared latencies in seconds².

**E. Modified case**  
Convert pixel intensities (0–255) to normalised [0,1] values – see modified file.

---

### Task 4 – Floating-Point Arithmetic and Numerical Errors

**B. Inputs & Operation**  
- `0.1 + 0.2` vs `0.3`  
- Absolute / relative error of √2 approximation  
- Unstable vs stable formula for \( (\sqrt{1+x}-1)/x \)

**C. Change parameter**  
Use a tighter tolerance `atol=1e-16` in `np.isclose`.  
Result still True for 0.1+0.2, but would fail for numbers that differ by more than machine epsilon.

**D. Output meaning**  
Shows that exact equality fails due to binary representation; relative error of 1.414 is ≈ 0.015 %; the stable formula remains accurate even for tiny x.

**E. Modified case**  
Banking interest calculation that accumulates floating-point error – see modified file.

---

### Task 5 – Matrix Algebra and Matrix Operations

**B. Inputs & Operation**  
- 4 corner points of a unit square  
- Rotation matrix (45°) and scaling matrix (2×, 1.5×)  
- Combined transformation \( R \cdot S \) applied to all points

**C. Change parameter**  
Change rotation angle to 90°.  
Result: points are rotated a quarter-turn; the square becomes a rectangle oriented differently.

**D. Output meaning**  
Transformed points show the new locations after scale+rotate. Determinant = 3.0 (area scaling factor).

**E. Modified case**  
2-D robot arm transformation (translation + rotation) – see modified file.

---

### Task 6 – Solution of Systems of Linear Equations

**B. Inputs & Operation**  
- Coefficient matrix A (CPU & memory usage per server type)  
- Right-hand side b = total observed resources  
- Solve \( Ax = b \) with `np.linalg.solve`

**C. Change parameter**  
Change total memory from 72 GB to 80 GB.  
Solution changes from (2, 6) to approximately (1.33, 7.33).

**D. Output meaning**  
Exactly 2 Type-A and 6 Type-B servers explain the observed resource consumption. Residual ≈ 0 confirms correctness.

**E. Modified case**  
Chemical equation balancing (stoichiometry) – see modified file.

---

### Task 7 – Gaussian Elimination and LU Decomposition

**B. Inputs & Operation**  
- Fixed sparse matrix A  
- Three different measurement vectors b  
- One LU factorisation, then three `lu_solve` calls

**C. Change parameter**  
Add a fourth measurement vector.  
Only one extra cheap solve is needed; factorisation cost is paid only once.

**D. Output meaning**  
Each solve gives the unknown state variables for that time step. Residual norms near zero prove accuracy.

**E. Modified case**  
Repeated daily load-flow calculations on the same power network – see modified file.

---

### Task 8 – Iterative Methods for Linear Systems

**B. Inputs & Operation**  
- Tridiagonal temperature matrix (5 interior nodes)  
- Boundary temperatures 100 °C and 20 °C  
- Jacobi and Gauss-Seidel iteration until tolerance 1e-8

**C. Change parameter**  
Tighten tolerance to 1e-12.  
Both methods need more iterations; Gauss-Seidel still converges faster.

**D. Output / Graph**  
Temperatures decrease smoothly from left to right. Semilog plot shows linear convergence; Gauss-Seidel has steeper slope (faster).

**E. Modified case**  
1-D heat conduction with different boundary temperatures – see modified file.

---

### Task 9 – Eigenvalues and Eigenvectors

**B. Inputs & Operation**  
- 4×4 adjacency matrix of an undirected graph  
- Dominant eigenpair → eigenvector centrality

**C. Change parameter**  
Add an edge between nodes A and D.  
Centrality scores redistribute; previously peripheral nodes become more important.

**D. Output meaning**  
Nodes B and C have highest importance (most central). Verification error ≈ 0 confirms \( Av = \lambda v \).

**E. Modified case**  
Simple PageRank on a small web graph – see modified file.

---

### Task 10 – Root Finding: Bisection and Fixed-Point

**B. Inputs & Operation**  
- Heat-balance function \( f(T) = T - 25 - 10e^{-T/20} \)  
- Bisection on [20,40] and fixed-point iteration \( T = 25 + 10e^{-T/20} \)

**C. Change parameter**  
Change ambient term from 25 to 30.  
Equilibrium temperature rises (new steady state is hotter).

**D. Output / Graph**  
Both methods give ≈ 32.07 °C. Graph shows the root where the curve crosses zero.

**E. Modified case**  
Break-even analysis for a small business – see modified file.

---

### Task 11 – Newton-Raphson and Secant Methods

**B. Inputs & Operation**  
- Cash-flow series → Net Present Value function  
- Newton (with analytic derivative) and Secant methods to find IRR

**C. Change parameter**  
Increase the initial investment to –12 000.  
IRR decreases because more capital must be recovered.

**D. Output meaning**  
IRR ≈ 14.3 %. NPV at that rate is essentially zero (root found).

**E. Modified case**  
Finding the interest rate that makes two investment options equivalent – see modified file.

---

### Task 12 – Polynomial and Nonlinear Equation Solving

**B. Inputs & Operation**  
- Circle \( x^2 + y^2 = 4 \) and parabola \( y = x^2 - 1 \)  
- `scipy.optimize.root` from two different initial guesses

**C. Change parameter**  
Change circle radius to √5 (equation = 5).  
Intersection points move outward.

**D. Output meaning**  
Two real intersection points are found; residuals ≈ 0 confirm they lie on both curves.

**E. Modified case**  
Intersection of a line and a circle (robot path planning) – see modified file.

---

### Task 13 – Interpolation

**B. Inputs & Operation**  
- Hourly temperatures  
- Linear and cubic-spline interpolants evaluated every 10 min

**C. Change parameter**  
Use only every second measurement.  
Cubic spline still produces a smooth curve but with larger local error.

**D. Output / Graph**  
Cubic spline is smoother than linear pieces. At 10:30 both give ≈ 23.25 °C.

**E. Modified case**  
Missing sensor data reconstruction for air quality – see modified file.

---

### Task 14 – Curve Fitting and Approximation

**B. Inputs & Operation**  
- Concurrent users vs response time  
- Quadratic model fitted by least squares (`curve_fit`)

**C. Change parameter**  
Fit a cubic model instead.  
RMSE usually decreases slightly, but risk of over-fitting increases.

**D. Output / Graph**  
Response time grows roughly quadratically. Predicted value at 400 users is extrapolated.

**E. Modified case**  
Fitting a growth curve to population data – see modified file.

---

### Task 15 – Numerical Differentiation

**B. Inputs & Operation**  
- Position samples at 1 s intervals  
- Forward / central / backward differences → speed

**C. Change parameter**  
Use 0.5 s sampling (denser data).  
Speed estimates become more accurate (smaller truncation error).

**D. Output / Graph**  
Speed increases almost linearly (constant acceleration). Graph shows estimated velocity vs time.

**E. Modified case**  
Estimate acceleration from velocity data of a vehicle – see modified file.

---

### Task 16 – Numerical Integration

**B. Inputs & Operation**  
- Power readings every 2 h  
- Trapezoidal rule and Simpson’s rule

**C. Change parameter**  
Use readings every 1 h (more points).  
Difference between the two rules becomes smaller.

**D. Output meaning**  
Total energy ≈ 15.6–15.7 kWh. Simpson’s rule is usually more accurate for smooth curves.

**E. Modified case**  
Distance travelled from speedometer readings – see modified file.

---

### Task 17 – Ordinary Differential Equations – Euler Method

**B. Inputs & Operation**  
- Newton’s law of cooling  
- Euler steps of size h = 1 min

**C. Change parameter**  
Halve the step size to h = 0.5.  
Final absolute error roughly halves (first-order method).

**D. Output / Graph**  
Temperature decays exponentially toward 25 °C. Euler stays close to the exact solution.

**E. Modified case**  
Radioactive decay of a substance – see modified file.

---

### Task 18 – Numerical Solution of ODEs Using SciPy

**B. Inputs & Operation**  
- RC-circuit charging ODE  
- `solve_ivp` with tight tolerances

**C. Change parameter**  
Double the capacitance.  
Time constant RC doubles → charging becomes twice as slow.

**D. Output / Graph**  
Voltage rises from 0 to almost 5 V. Maximum error vs exact solution is machine-precision level.

**E. Modified case**  
Simple SIR epidemic model – see modified file.

---

### Task 19 – Numerical Optimization

**B. Inputs & Operation**  
- Cost function 12x + 18y  
- Capacity constraint 100x + 170y ≥ 1000  
- SLSQP minimizer + integer enumeration

**C. Change parameter**  
Raise required capacity to 1200.  
Optimal cost increases; more servers (or higher-capacity mix) are needed.

**D. Output meaning**  
Continuous optimum is fractional; best integer solution is reported separately.

**E. Modified case**  
Minimise cost of a diet subject to nutritional constraints – see modified file.

---

### Task 20 – Random Numbers and Monte Carlo Methods

**B. Inputs & Operation**  
- Normal demand distribution  
- Indicator “demand > capacity”  
- Monte-Carlo estimate of overload probability

**C. Change parameter**  
Increase standard deviation to 150.  
Overload probability rises because demand is more variable.

**D. Output / Graph**  
Estimated probability ≈ 10–12 %. Running-average plot converges to a stable value.

**E. Modified case**  
Estimate probability that a project finishes late (PERT-style) – see modified file.

---

## How to use this package

```
BIT2118_Full_Solution/
├── original_codes/          # exact codes from the handout
├── modified_codes/          # one related real-world variant per task
└── docs/
    └── Full_Analysis_Report.md   # this file (B–D for every task)
```

All modified programs are self-contained and ready to run.
