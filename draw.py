import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen() 
s.bgcolor("#0C0C22")
t.speed(0)
n = 36
h = 0
t.setx(-450)
for i in range(2):
    for i in range(80):
        c = colorsys.hsv_to_rgb(h, 1, 0.9)
        h += 1/n
        t.color(c)
        t.lt(145)
        t.circle(180, 360)
        for j in range(5):
            t.fd(350)
            t.lt(150)
    t.setx(450)



    
   