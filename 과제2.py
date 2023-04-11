import cordinate_plane as cp
import turtle as p


cp.line (-800,0,800,0)
cp.line (0,-500,0,500)

i=-700
while i <600:
    i = i+100
    cp.line(i,-5,i,5)
    if i !=0:
        cp.write(i-10,-20,i)
        
i=-600
while i <500:
    i = i+100
    cp.line(-5,i,5,i)
    if i !=0:
        cp.write(7,i-5,i)


p.up()
p.goto(0,0)
p.color("red")

a = float (input("a값 입력: "))
t = int (input("t값 입력: "))
q = int (input("q값 입력: "))


x = -500

while x <= 500:
    y = (a * (x - t )*(x - t) )+q
    p.goto(x,y)
    x +=1
    p.down()
