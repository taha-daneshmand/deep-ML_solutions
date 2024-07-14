def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if not matrix or not matrix[0]:
        return []

    if mode == 'row':
        means = [sum(row) / len(row) for row in matrix]
    elif mode == 'column':
        num_columns = len(matrix[0])
        means = [sum(row[i] for row in matrix) / len(matrix) for i in range(num_columns)]
    else:
        raise ValueError("Mode must be either 'row' or 'column'")

    means = [round(mean, 1) for mean in means]

    return means
