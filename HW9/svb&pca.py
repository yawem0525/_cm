# 1. 用特徵值分解實作 SVD (簡化版：A^T A 的特徵向量)
def simple_svd(A):
    # V 是 A^T A 的特徵向量
    eig_vals, V = eig(A.T @ A)
    # Sigma 是特徵值的平方根
    sigma = np.sqrt(np.abs(eig_vals))
    # U 是 A V Sigma^-1
    U = A @ V @ np.linalg.inv(np.diag(sigma))
    return U, sigma, V.T

# 2. PCA 主成分分析
def manual_pca(data, k):
    # 數據中心化 (Centering)
    mean_centered = data - np.mean(data, axis=0)
    # 使用 SVD 分解
    U, S, Vt = np.linalg.svd(mean_centered)
    # 取前 k 個主成分
    return mean_centered @ Vt.T[:, :k]

# 測試數據
data = np.array([[2.5, 2.4], [0.5, 0.7], [2.2, 2.9], [1.9, 2.2], [3.1, 3.0]])
print("PCA 降維結果:\n", manual_pca(data, 1))
