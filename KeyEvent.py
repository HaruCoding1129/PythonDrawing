import turtle as t

# 터틀의 기본방향은 오른쪽으로부터 시작합니다.
# 따라서 방향을 90도, 180도 270도를 틀면 윗쪽, 왼쪽, 아랫쪽 방향이 됩니다. 

# 오른쪽
def right():
    t.setheading(0)
    t.forward(10)

# 위
def up():
    t.setheading(90)
    t.forward(10)

# 왼쪽
def left():
    t.setheading(180)
    t.forward(10)

# 아래
def down():
    t.setheading(270)
    t.forward(10)

# 1번키 : 파란색
def blue_1():
    t.pencolor("blue")

# 2번키 : 빨강색
def red_2():
    t.pencolor("red")

# 3번키 : 검정색
def black_3():
    t.pencolor("black")
    
# 키 등록 : ﻿onkey(fun, key)﻿
# fun 에는 위에서 만든 함수이름을 써주면 됩니다.
# key 에는 설정하고 싶은 키를 입력하면 됩니다.

t.onkey(up, "Up")
t.onkey(down, "Down")
t.onkey(right, "Right")
t.onkey(left, "Left")
t.onkey(blue_1, "1")
t.onkey(red_2, "2")
t.onkey(black_3, "3")

# onkey로 등록된 키를 누르면 listen()에게 값이 전달이 됩니다.
# listen()은 onkey로 부터 전달되는 값을 받고 반응하게 해줍니다.
# listen()을 생략하면 키보드를 아무리 눌려도 어떤 반응도 나타나지 않습니다.

t.listen()
