import numpy as np
def evals(A, B):
    return np.linalg.eigvalsh(A + B)

a, b = np.random.rand(8), np.random.rand(8) # List of 8 random values between 0-1
A = np.diag(a) # Computes a 8x8 matrix with the 8 values along the diagonal
B = np.diag(b)
X = A + B
values = evals(A, B)
assert np.allclose(sorted(values), sorted(a+b)) # Checks if the diagonals are similiar to the list of eigenvalues

