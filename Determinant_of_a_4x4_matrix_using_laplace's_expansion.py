from typing import List, Union

MatrixType = List[List[Union[int, float]]]

def determinant_4x4(matrix: MatrixType) -> float:
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for c in range(len(matrix)):
        minor = [row[:c] + row[c+1:] for row in matrix[1:]]
        cofactor = ((-1) ** c) * determinant_4x4(minor)
        det += matrix[0][c] * cofactor
    return det
