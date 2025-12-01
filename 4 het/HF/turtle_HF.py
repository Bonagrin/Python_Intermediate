from turtle import *

Screen().bgcolor("orange")
speed(0)

width(4)
color("red")

for i in range(40):
    forward(i)
    right(59)

j = i + 10
width(2)
color("green")

while j >= 0:
    forward(j)
    right(59)
    j -= 1
    
done()
