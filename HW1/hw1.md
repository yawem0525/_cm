## 使用程式驗證微積分基本定理（Fundamental Theorem of Calculus）

### 一、實驗目的
本實驗目的為利用程式進行數值計算，驗證微積分基本定理，說明「積分與微分互為反運算」的性質。

---

### 二、微積分基本定理說明

#### （一）第一基本定理
若定義  
\[
F(x)=\int_a^x f(t)\,dt
\]
則  
\[
F'(x)=f(x)
\]

亦即：**先積分再微分，會回到原來的函數**。

---

#### （二）第二基本定理
若 \(F'(x)=f(x)\)，則  
\[
\int_a^b f(x)\,dx = F(b)-F(a)
\]

---

### 三、實驗方法

1. 選擇函數  
   \[
   f(x)=x^2
   \]

2. 使用數值積分（梯形法）計算  
   \[
   F(x)=\int_0^x f(t)\,dt
   \]

3. 使用數值微分（中央差分法）近似計算  
   \[
   F'(x)
   \]

4. 比較 \(F'(x)\) 與原函數 \(f(x)\) 的數值是否一致。

---

### 四、實驗程式碼（Python）

```python
import numpy as np

def f(x):
    return x**2

def F(x, n=10000):
    t = np.linspace(0, x, n)
    y = f(t)
    return np.trapz(y, t)

def derivative_F(x, h=1e-5):
    return (F(x + h) - F(x - h)) / (2 * h)

test_points = [0.5, 1.0, 2.0, 3.0]

print("x     f(x)     F'(x)")
for x in test_points:
    print(x, f(x), derivative_F(x))
