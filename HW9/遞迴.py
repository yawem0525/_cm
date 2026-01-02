def get_determinant(matrix):
    # 基本情況：2x2 矩陣
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for c in range(len(matrix)):
        # 取得餘因子矩陣 (Minor)
        minor = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1)**c) * matrix[0][c] * get_determinant(minor)
    return det

# 測試
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"遞迴行列式: {get_determinant(A)}") # 應為 0
