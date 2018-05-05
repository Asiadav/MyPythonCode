import arcade
import time
import random
import math

width = 480
height = 360
cWidth = 130
cHeight = 25

arcade.open_window(width, height, "Screen Saver")

arcade.start_render()
def thing(x,y):
    arcade.set_background_color((255,255,255))
    arcade.draw_rectangle_filled(width/2,height/2,width,height,(0,0,0))
    #arcade.draw_rectangle_filled(x,y,cWidth,cHeight,(200,0,100))
    arcade.draw_text("LOGO",x, y, (200,0,100), 40, width=cWidth, align="center",anchor_x="center", anchor_y="center")
    arcade.draw_point(x,y,10,(250,250,250))

global xdir
global ydir
global x
global y
xdir = 1
ydir = 1
x = width/2
y = height/2
def run(time):
    spd = 2
    global xdir
    global ydir
    global x
    global y

    if x > width - cWidth/2:
        xdir = 0
    if y > height-cHeight/2:
        ydir = 0
    if x < cWidth/2:
        xdir = 1
    if y < cHeight/2 + 10:
        ydir = 1
    if xdir == 1:
        x += spd
    if xdir == 0:
        x -= spd
    if ydir == 1:
        y += spd
    if ydir == 0:
        y -= spd

    thing(x,y)

arcade.schedule(run,1/60)
arcade.run()