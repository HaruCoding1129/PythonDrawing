import turtle as t

t.speed(0)

t.left(90)

def draw_circle(color, length, degree):
        
    t.color(color)
    t.begin_fill()
    t.circle(length, degree)
    t.end_fill()


draw_circle("red", 100, 180)
draw_circle("blue", 100, 180)

draw_circle("blue", 50, 360)
t.goto(-100,0)
draw_circle("red", 50, 360)



t.penup()
t.goto(100,100)
t.pendown()
