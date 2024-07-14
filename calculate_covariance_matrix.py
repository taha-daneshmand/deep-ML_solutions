import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    data = np.array(vectors)
    
    means = np.mean(data, axis=1)
    
    centered_data = data - means[:, np.newaxis]
    
    n = data.shape[1]
    cov_matrix = np.dot(centered_data, centered_data.T) / (n - 1)
    
    cov_matrix = np.round(cov_matrix, 1)
    
    return cov_matrix.tolist()
