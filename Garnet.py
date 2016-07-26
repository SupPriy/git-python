import turtle
t=turtle.Pen()
t.pensize(110)
red=1
green=0.5
blue=1
for i in range(1,10):
    t.color(red,green,blue)
    t.forward(200);
    t.right(100);
    t.forward(200);
    t.right(100);
    red=red - 0.1
    green=0.5
    blue=1
t.color(1,1,0)
t.up()
t.right(48)
t.forward(135)
t.down()
t.pensize(50)
t.circle(15)
 
