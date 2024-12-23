import time

for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("MERRY CHRISTMAS")

      
    
n=10
for i in range(0, n):
    for j in range(1,n-i):
        print(" ",end="")
    print("*",end="")
    for k in range(0,i):
        print("!",end="")
    for j in range(1,i):
        print("!",end="")
    if i>0:
        print("*", end="")
    print()    













import turtle
import colorsys
t=turtle.Turtle()
s=turtle.Screen().bgcolor("black")
t.speed(-5)
n=70
h=0
for i in range(360):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range(2):
        t.left(2)
        t.circle(100)
