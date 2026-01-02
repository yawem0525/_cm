# 數學與程式的交匯：謝爾賓斯基三角形研究報告

---

## 1. 研究主題簡介

謝爾賓斯基三角形（Sierpinski Triangle）是分形幾何（Fractal Geometry）中最著名的圖形之一。  
它展示了如何透過**簡單的遞迴規則**，在有限的空間內創造出**無限複雜且具自我相似性**的結構。

---

## 2. 數學原理分析

### 2.1 幾何構造

謝爾賓斯基三角形的生成流程如下：

1. 取一個實心正三角形  
2. 連結三邊的中點，將原三角形分割成四個全等小三角形  
3. 移除中間倒置的小三角形  
4. 對剩下的三個正立小三角形重複上述步驟（遞迴）

---

### 2.2 核心數學性質

#### （1）豪斯多夫維度（Hausdorff Dimension）

謝爾賓斯基三角形並非傳統的一維或二維圖形，其分形維度為：

\[
D = \frac{\ln 3}{\ln 2} \approx 1.585
\]

此結果說明該圖形的維度介於 1 與 2 之間。

---

#### （2）面積與周長的極限行為

- **面積**：當遞迴次數 \( n \to \infty \) 時，面積趨近於 **0**
- **周長**：當遞迴次數 \( n \to \infty \) 時，周長趨近於 **無限大**

---

## 3. 程式實作（Python）

以下使用 Python 的 `turtle` 模組，透過**遞迴演算法**來繪製謝爾賓斯基三角形。

```python
import turtle

def draw_sierpinski(length, depth):
    """
    遞迴繪製謝爾賓斯基三角形
    :param length: 邊長
    :param depth: 遞迴深度
    """
    if depth == 0:
        # 基本繪製單元：正三角形
        for _ in range(3):
            turtle.forward(length)
            turtle.left(120)
    else:
        draw_sierpinski(length / 2, depth - 1)

        turtle.forward(length / 2)
        draw_sierpinski(length / 2, depth - 1)

        turtle.backward(length / 2)
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.right(60)
        draw_sierpinski(length / 2, depth - 1)

        # 回到原始位置
        turtle.left(60)
        turtle.backward(length / 2)
        turtle.right(60)

# 初始化畫布
turtle.speed(0)
turtle.setup(600, 600)
turtle.penup()
turtle.goto(-200, -150)
turtle.pendown()

# 執行繪製（建議深度 4～5）
draw_sierpinski(400, 4)
turtle.hideturtle()
turtle.done()
