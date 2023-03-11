from turtle import *
for i in range(6):
    print(i, i%3)
    if i%3==0:
        color('blue')
    elif i%3==1:
        color('green')
    else:
        color('yellow')
    forward(100)
    left(60)
mainloop()