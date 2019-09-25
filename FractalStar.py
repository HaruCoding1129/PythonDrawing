import turtle as t

def draw_star(length, step):
    if step == 0:
      return
    else :
      for i in range(0,5):
        t.forward(length)
        draw_star(length/3, step-1)
        t.right(144)

t.speed(0)
t.bgcolor("black")
t.color("yellow")
draw_star(200, 3)
