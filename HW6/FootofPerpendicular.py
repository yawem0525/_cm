def get_perpendicular_foot(p, line):
    # 垂直線的斜率與原線乘積為 -1
    # 垂直線方程式為: Bx - Ay + (Ay1 - Bx1) = 0
    perp_line = Line(line.B, -line.A, line.A * p.y - line.B * p.x)
    return intersect_lines(line, perp_line)

# 驗證畢氏定理
def verify_pythagoras(p_external, line):
    foot = get_perpendicular_foot(p_external, line)
    # 取線上另一點
    p_on_line = Point(foot.x + line.B, foot.y - line.A) 
    
    # 計算三邊長
    a = math.dist((p_external.x, p_external.y), (foot.x, foot.y))
    b = math.dist((foot.x, foot.y), (p_on_line.x, p_on_line.y))
    c = math.dist((p_external.x, p_external.y), (p_on_line.x, p_on_line.y))
    
    print(f"a^2 + b^2 = {a**2 + b**2:.4f}")
    print(f"c^2 = {c**2:.4f}")
    return math.isclose(a**2 + b**2, c**2)
