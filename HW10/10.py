import cmath

def dft(f):
    """
    離散傅立葉正轉換 (DFT)
    實作公式: F[k] = Σ (n=0 to N-1) f[n] * exp(-i * 2π * k * n / N)
    """
    N = len(f)
    F = []
    for k in range(N):
        sum_val = complex(0, 0)
        for n in range(N):
            # 計算複數指數部分: e^(-i * 2 * pi * k * n / N)
            angle = -2j * cmath.pi * k * n / N
            sum_val += f[n] * cmath.exp(angle)
        F.append(sum_val)
    return F

def idft(F):
    """
    離散傅立葉逆轉換 (IDFT)
    實作公式: f[n] = (1/N) * Σ (k=0 to N-1) F[k] * exp(i * 2π * k * n / N)
    """
    N = len(F)
    f = []
    for n in range(N):
        sum_val = complex(0, 0)
        for k in range(N):
            # 計算複數指數部分: e^(i * 2 * pi * k * n / N)
            angle = 2j * cmath.pi * k * n / N
            sum_val += F[k] * cmath.exp(angle)
        # 注意：逆轉換通常需要除以樣本數 N
        f.append(sum_val / N)
    return f

# --- 驗證部分 ---

# 1. 定義原始函數 f (這裡我們用一組簡單的數值模擬訊號)
original_f = [1.0, 2.0, 3.0, 4.0, 5.0, 4.0, 3.0, 2.0]
print(f"原始數列 f: {original_f}")

# 2. 進行正轉換 (f -> F)
transformed_F = dft(original_f)
print("\n正轉換後的結果 F (前 3 項):")
for i in range(min(3, len(transformed_F))):
    print(f"  F[{i}] = {transformed_F[i]:.3f}")

# 3. 進行逆轉換回來的結果 (F -> f_back)
recovered_f = idft(transformed_F)

# 4. 驗證結果是否一致
print("\n逆轉換回來的結果 f':")
# 由於浮點數運算會有微小誤差，我們取實部並四捨五入
recovered_f_real = [round(val.real, 10) for val in recovered_f]
print(recovered_f_real)

# 檢查原始與恢復的是否相同
is_same = all(abs(o - r) < 1e-10 for o, r in zip(original_f, recovered_f_real))
print(f"\n驗證結果：{'成功！恢復後的函數與原函數相同' if is_same else '失敗'}")
