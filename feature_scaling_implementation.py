import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    standardized_data = (data - mean) / std

    min_vals = np.min(data, axis=0)
    max_vals = np.max(data, axis=0)
    normalized_data = (data - min_vals) / (max_vals - min_vals)

    standardized_data = np.round(standardized_data, 4)
    normalized_data = np.round(normalized_data, 4)

    return standardized_data, normalized_data
