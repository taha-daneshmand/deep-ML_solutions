import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    np_array = np.array(a)
    
    reshaped_array = np_array.reshape(new_shape)
    
    reshaped_matrix = reshaped_array.tolist()
    
    return reshaped_matrix
