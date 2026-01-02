import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x:.2f}, {self.y:.2f})"

class Line:
    """一般式 Ax + By + C = 0"""
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    @classmethod
    def from_points(cls, p1, p2):
        A = p1.y - p2.y
        B = p2.x - p1.x
        C = p1.x * p2.y - p2.x * p1.y
        return cls(A, B, C)

class Circle:
    def __init__(self, center, r):
        self.center = center
        self.r = r

def intersect_lines(l1, l2):
    det = l1.A * l2.B - l2.A * l1.B
    if abs(det) < 1e-9: return None  # 平行
    x = (l1.B * l2.C - l2.B * l1.C) / det
    y = (l2.A * l1.C - l1.A * l2.C) / det
    return Point(x, y)

def intersect_line_circle(line, circle):
    # 將圓心移到原點進行計算，最後再移回
    h, k = circle.center.x, circle.center.y
    r = circle.r
    # 調整直線 C 項以適應圓心偏移: A(x+h) + B(y+k) + C = 0 -> Ax + By + (Ah + Bk + C) = 0
    C_prime = line.A * h + line.B * k + line.C
    
    A, B = line.A, line.B
    dist_sq = C_prime**2 / (A**2 + B**2)
    if dist_sq > r**2 + 1e-9: return [] # 無交點
    
    # 計算垂足 (Projection)
    x0 = -A * C_prime / (A**2 + B**2)
    y0 = -B * C_prime / (A**2 + B**2)
    
    if abs(dist_sq - r**2) < 1e-9: # 切點
        return [Point(x0 + h, y0 + k)]
    
    d = math.sqrt((r**2 - dist_sq) / (A**2 + B**2))
    return [
        Point(x0 + B*d + h, y0 - A*d + k),
        Point(x0 - B*d + h, y0 + A*d + k)
    ]
