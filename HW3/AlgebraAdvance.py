import cmath

def root3(a, b, c, d):
    """
    計算三次多項式 ax^3 + bx^2 + cx + d = 0 的三個根
    （包含複數根）
    """
    if a == 0:
        raise ValueError("a 不能為 0，否則不是三次多項式")

    # 轉為降次形式 y^3 + py + q = 0
    p = (3*a*c - b*b) / (3*a*a)
    q = (2*b**3 - 9*a*b*c + 27*a*a*d) / (27*a*a*a)

    # 判別式
    Δ = (q/2)**2 + (p/3)**3

    # Cardano 公式（使用 cmath 處理複數）
    u = cmath.sqrt(Δ)
    C = (-q/2 + u)**(1/3)
    D = (-q/2 - u)**(1/3)

    # 三個立方根的單位根
    omega = complex(-0.5, cmath.sqrt(3)/2)

    y1 = C + D
    y2 = omega*C + omega.conjugate()*D
    y3 = omega.conjugate()*C + omega*D

    # 轉回 x
    shift = b / (3*a)
    x1 = y1 - shift
    x2 = y2 - shift
    x3 = y3 - shift

    return x1, x2, x3
