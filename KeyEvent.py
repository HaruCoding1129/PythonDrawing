import turtle as t


# ========== 방향키 ==========
def right():
    t.setheading(0)
    t.forward(10)

def up():
    t.setheading(90)
    t.forward(10)

def left():
    t.setheading(180)
    t.forward(10)

def down():
    t.setheading(270)
    t.forward(10)
    

# ========== 색상변경 ==========
def blue_1():
    t.pencolor("blue")

def red_2():
    t.pencolor("red")

def black_3():
    t.pencolor("black")

    
# ========== 도형그리기 ==========
def square_4():
  for i in range(0,4):
    t.forward(200) 
    t.left(90) 

def circle_5():
  t.circle(100)

def star_6():
  for i in range(0,5):
     t.forward(200)
     t.right(144)

    
# ========== 펜 Up & Down ==========
def square_q():
  t.penup()

def circle_w():
  t.down()


# ========== 키 등록 ==========

#방향키
t.onkey(up, "Up")
t.onkey(down, "Down")
t.onkey(right, "Right")
t.onkey(left, "Left")

#색상변경
t.onkey(blue_1, "1")
t.onkey(red_2, "2")
t.onkey(black_3, "3")

#도형그리기
t.onkey(square_4, "4")
t.onkey(circle_5, "5")
t.onkey(star_6, "6")

#펜 Up & Down
t.onkey(square_4, "q")
t.onkey(circle_5, "w")


# ========== listen() 잊지 마세요! ==========
t.listen()
