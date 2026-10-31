import numpy as np

# Store the four square corners as rows of two-dimensional [x, y] coordinates.
points = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0]
])

# Convert the rotation angle from degrees to radians for NumPy's trigonometric functions.
angle = np.deg2rad(45)

# Build the 2-D rotation matrix for a counterclockwise 45-degree rotation.
rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])

# Build a diagonal matrix that doubles x-coordinates and scales y-coordinates by 1.5.
scale = np.array([
    [2.0, 0.0],
    [0.0, 1.5]
])

# Combine scaling and then rotation using matrix multiplication.
transformation = rotation @ scale

# Apply the combined transform to each row-stored point using the transpose.
transformed_points = points @ transformation.T

# Show the input, combined transform, transformed coordinates, and area scale factor.
print("Original points:\n", points)
print("Transformation matrix:\n", transformation)
print("Transformed points:\n", transformed_points)
print("Determinant:", np.linalg.det(transformation))
