#좌표평면 
#cordinate_plane 모듈파일

import turtle as p

p.speed(0)  # 0빠름 1느림 
p.hideturtle
p.color("black")
p.shape("turtle")

def line(x1,y1,x2,y2):
    p.up()
    p.goto(x1,y1)
    p.down()
    p.goto(x2,y2)
    return 

def write(x,y,text):
    p.up()
    p.goto(x,y)
    p.down()
    p.write(text)
    return 
