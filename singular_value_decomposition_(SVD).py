import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    A_T_A = A.T @ A
    
    theta = 0.5 * np.arctan2(2 * A_T_A[0, 1], A_T_A[0, 0] - A_T_A[1, 1])
    
    J = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])
    
    A_prime = J.T @ A_T_A @ J
    
    singular_values = np.sqrt(np.diag(A_prime))

    return J, singular_values, J.T
