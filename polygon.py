from turtle import *
side=int(input('How many side for your polygon'))
size=int(input('size of 1 side in px ='))
for i in range(side):
    forward(size)
    left(360/side)
    dot(10,'orange')
mainloop()
