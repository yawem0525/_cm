import numpy as np
from scipy.linalg import lu, svd, eig

def lu_determinant(A):
    P, L, U = lu(A)
    # det(A) = det(P) * det(L) * det(U)
    # det(L) 為 1, det(U) 為對角線乘積, det(P) 為置換次數決定正負
    det_u = np.prod(np.diag(U))
    # 計算 P 的行列式 (這裡簡化處理)
    return np.linalg.det(P) * det_u

A = np.array([[4, 3], [6, 3]])
print(f"LU 分解行列式: {lu_determinant(A)}")

# 驗證分解：A = L * U (忽略 P 以簡化)
P, L, U = lu(A)
print("驗證 LU 分解:", np.allclose(A, P @ L @ U))
