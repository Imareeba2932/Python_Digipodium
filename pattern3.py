from turtle import *
for i in range(6):
    print(i, i%2)
    if i%2==0:
        color('blue')
    else:
        color('yellow')
    forward(100)
    left(60)
mainloop()