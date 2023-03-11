from turtle import *
speed('fastest')
pencolor('orange')
bgcolor('black')
pensize(1)
for i in range(80):
    backward(i)
    left(120)
    for j in range(5):
        forward(i)
        left(180)
mainloop()