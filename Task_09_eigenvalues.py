import numpy as np

# Adjacency matrix for a small undirected network.
# Node order: A, B, C, D
A = np.array([
    [0., 1., 1., 0.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [0., 1., 1., 0.]
])

# Compute the eigenvalues and corresponding eigenvectors of the network matrix.
eigenvalues, eigenvectors = np.linalg.eig(A)

# Select the eigenpair with the largest real eigenvalue for eigenvector centrality.
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
dominant_vector = np.abs(np.real(eigenvectors[:, index]))
# Normalize scores so all node-importance values sum to one.
centrality = dominant_vector / dominant_vector.sum()

nodes = ["A", "B", "C", "D"]

# Report each node's normalized centrality and verify the eigenvector equation.
print("Dominant eigenvalue:", dominant_value)
print("Eigenvector-based importance:")
for node, score in zip(nodes, centrality):
    print(f"{node}: {score:.4f}")

# Verify Av = lambda*v
v = np.real(eigenvectors[:, index])
print("Verification error:",
      np.linalg.norm(A @ v - dominant_value * v))
