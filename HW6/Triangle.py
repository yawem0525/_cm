class Triangle:
    def __init__(self, p1, p2, p3):
        self.points = [p1, p2, p3]

    def translate(self, dx, dy):
        for p in self.points:
            p.x += dx
            p.y += dy

    def scale(self, factor, center=Point(0, 0)):
        for p in self.points:
            p.x = center.x + (p.x - center.x) * factor
            p.y = center.y + (p.y - center.y) * factor

    def rotate(self, angle_rad, center=Point(0, 0)):
        s, c = math.sin(angle_rad), math.cos(angle_rad)
        for p in self.points:
            # 移至原點
            tx, ty = p.x - center.x, p.y - center.y
            # 旋轉矩陣運算
            p.x = tx * c - ty * s + center.x
            p.y = tx * s + ty * c + center.y
