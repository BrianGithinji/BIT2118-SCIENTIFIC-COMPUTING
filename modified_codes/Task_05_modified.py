"""
Task 5 – Modified real-world case
2-D robot-arm pose transformation:
translate the end-effector by (3,1) then rotate 30 degrees about the origin.
"""
import numpy as np

# Store the end-effector path as a sequence of 2-D points.
points = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.5, 0.5],
    [2.0, 0.5]
])

# Add a homogeneous coordinate of 1 to each point so translations use matrix products.
ones = np.ones((points.shape[0], 1))
pts_h = np.hstack([points, ones])

# Convert the requested rotation angle to radians and construct its homogeneous matrix.
theta = np.deg2rad(30)
R = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta),  np.cos(theta), 0],
    [0,              0,             1]
])

# Construct a homogeneous matrix that translates points by (3, 1).
T = np.array([
    [1, 0, 3],
    [0, 1, 1],
    [0, 0, 1]
])

# Apply translation first and then rotation to each point using column-vector convention.
transformed = (R @ T @ pts_h.T).T

# Display the input path and the transformed 2-D coordinates.
print("Original points:\n", points)
print("Transformed points:\n", transformed[:, :2])
