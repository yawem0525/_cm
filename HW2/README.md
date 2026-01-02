## 二次多項式根的程式求解與驗證

### 一、問題說明
給定二次多項式  
\[
f(x) = ax^2 + bx + c
\]

請撰寫一個 Python 函數 `root2(a, b, c)`，利用二次方程式的根公式計算其兩個根。  
當判別式為負數時，也必須能正確回傳**複數根**。

---

### 二、數學原理

二次方程式的根公式為  
\[
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\]

其中  
\[
\Delta = b^2 - 4ac
\]

- 若 \(\Delta > 0\)：兩個相異實根  
- 若 \(\Delta = 0\)：重根  
- 若 \(\Delta < 0\)：一對共軛複數根  

因此在程式中必須使用 `cmath.sqrt`，才能處理負數判別式。

---

### 三、程式設計說明

- 使用 `cmath.sqrt()` 計算平方根（支援複數）
- 回傳兩個根
- 使用 `cmath.isclose()` 驗證將根代回原多項式後，結果是否接近 0

---

### 四、Python 程式碼

```python
import cmath

def root2(a, b, c):
    """
    計算二次多項式 ax^2 + bx + c = 0 的兩個根
    """
    if a == 0:
        raise ValueError("a 不能為 0，否則不是二次多項式")

    D = b**2 - 4*a*c
    sqrt_D = cmath.sqrt(D)

    x1 = (-b + sqrt_D) / (2*a)
    x2 = (-b - sqrt_D) / (2*a)

    return x1, x2
