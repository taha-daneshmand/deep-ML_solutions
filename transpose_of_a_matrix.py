def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    rows = len(a)
    cols = len(a[0]) if rows > 0 else 0
    
    b = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            b[j][i] = a[i][j]
    
    return b
