from turtle import *
def pentagon(size):
    fillcolor('red')
    begin_fill()
    for i in range(5):
        forward(size)
        left(72)
    end_fill()
def triangle(size=50):
    fillcolor('yellow')
    begin_fill()
    for i in range(3):
        forward(size)
        left(120)
    end_fill()
for i in range(6):
    if i%2==0:
        pentagon(100)
    else:
        triangle(100)
    left(60)
mainloop()