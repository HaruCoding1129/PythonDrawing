import turtle as t
import random as r # 랜덤 모듈 불러오기

# 색상 리스트 만들기
color = ["red", "blue", "white", "green", "pink", "purple", "yellow", "Medium Aquamarine"]

# 배경색 검정색으로 지정하기
t.bgcolor("black")

# 빠르게 그리기
t.speed(0)

for i in range(30):
  # x, y 랜덤 좌표 얻기
  ran_x = r.randint(-350, 300) # x 좌표 범위 : -350 ~ 300
  ran_y = r.randint(-300, 350) # y 좌표 범위 : -300 ~ 350

  # 색을 정하기 위한 랜덤숫자 얻기
  ran_color = r.randint(0, len(color)-1)

  # 랜덤으로 길이 정하기
  ran_forward = r.randint(30, 150)

  t.color(color[ran_color])
  t.begin_fill()
  t.penup()
  t.goto(ran_x, ran_y)
  t.pendown()
  for i in range(0,5):
    
    t.forward(ran_forward)
    t.right(144)
  t.end_fill()