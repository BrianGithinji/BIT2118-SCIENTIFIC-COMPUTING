import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Store observed server response times corresponding to each concurrent-user count.
users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
response_ms = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)

# Define a quadratic model whose coefficients are fitted to the measured data.
def model(x, a, b, c):
    return a*x**2 + b*x + c

# Estimate the model coefficients and predict responses at the observed user counts.
parameters, covariance = curve_fit(model, users, response_ms)
a, b, c = parameters

predicted = model(users, a, b, c)
# Calculate root-mean-square fitting error in milliseconds.
rmse = np.sqrt(np.mean((response_ms - predicted)**2))

print(f"Fitted model: y = {a:.6f}x^2 + {b:.4f}x + {c:.2f}")
print(f"RMSE: {rmse:.2f} ms")
print(f"Predicted response at 400 users: {model(400, a, b, c):.2f} ms")

# Plot observed responses and the fitted model, extending the curve to 400 users.
x_plot = np.linspace(users.min(), 400, 300)
plt.scatter(users, response_ms, label="Measurements")
plt.plot(x_plot, model(x_plot, a, b, c), label="Fitted curve")
plt.xlabel("Concurrent users")
plt.ylabel("Response time (ms)")
plt.title("Server response-time curve fitting")
plt.legend()
plt.grid(True)
plt.savefig("Task_14_curve_fitting.png")
plt.show()
