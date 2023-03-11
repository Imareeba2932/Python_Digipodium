from turtle import *
speed('fastest')
pencolor('yellow')
bgcolor('black')
pensize(3)
for i in range(100):
    backward(i)
    left(60)
    circle(i)
mainloop()
