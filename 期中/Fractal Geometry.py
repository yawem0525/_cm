import turtle

def draw_sierpinski(length, depth):
    if depth == 0:
        # 基本情況：畫一個填滿的等邊三角形
        for _ in range(3):
            turtle.forward(length)
            turtle.left(120)
    else:
        # 遞迴情況：將大三角形拆分為三個小三角形
        # 繪製左下角的子三角形
        draw_sierpinski(length / 2, depth - 1)
        
        turtle.forward(length / 2)
        # 繪製右下角的子三角形
        draw_sierpinski(length / 2, depth - 1)
        
        turtle.backward(length / 2)
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.right(60)
        # 繪製上方的子三角形
        draw_sierpinski(length / 2, depth - 1)
        
        # 回到起始點
        turtle.left(60)
        turtle.backward(length / 2)
        turtle.right(60)

def main():
    turtle.speed(0) # 設置最快繪圖速度
    turtle.penup()
    turtle.goto(-200, -150) # 移動到適合的起始位置
    turtle.pendown()
    
    # 設定遞迴深度（建議 3-5 階，太高會跑很久）
    level = 4 
    draw_sierpinski(400, level)
    
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
