from turtle import *

speed(20)
color_list = ['red', 'blue']
len(color_list)

n = 2

for j in range (5):
    n = n+1
    color(color_list[j % len(color_list)])
    for i in range(n):
        left(360/n)
        forward(100)

mainloop()
