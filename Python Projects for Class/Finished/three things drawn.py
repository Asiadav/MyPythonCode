import arcade
import random
import math

arcade.open_window(600, 400, "Three Things")
arcade.set_background_color(arcade.color.BLUE)

x = 0
y = 0
def point_based_triangle(x, y, dist, color):
    x1 = x
    y1 = y+dist
    root3 = math.sqrt(3)
    x2 = x - (root3*(dist/2))
    y2 = y - dist/2
    x3 = x + (x - x2)
    y3 = y2

    arcade.draw_triangle_filled(x1,y1,x2,y2,x3,y3,color)

def make_tree(x,y,size):
    height = size/2
    width = size/5
    x1 = x
    y1 = y - 3*height/4


    arcade.draw_rectangle_filled(x1,y1,width,height/2,(200,150,100))

    point_based_triangle(x,y-2*width/3,size/3,arcade.color.FOREST_GREEN)

    point_based_triangle(x,y+height/16,size/4,arcade.color.FOREST_GREEN)

def draw_house(x,y,size):
    arcade.draw_rectangle_filled(x,y-40,size,size,(150,100,150))
    arcade.draw_rectangle_filled(x+10,y-80,size/4,size/2,(50,150,100))
    point_based_triangle(x,y+size/2,2*size/3,arcade.color.RED)

def clouds(x,y,size):
    arcade.draw_circle_filled(x,y,size,(255,255,255))
    arcade.draw_circle_filled(x+30,y+10,size * 1.5,(255,255,255))
    arcade.draw_circle_filled(x-10,y+20,size* 1.3,(255,255,255))
    arcade.draw_circle_filled(x+20,y+30,size * 1.2,(255,255,255))
    arcade.draw_circle_filled(x-10,y-10,size * 1.4,(255,255,255))

def draw_these(time):
    arcade.start_render()
    global x
    global y
    arcade.draw_rectangle_filled(400,50,800,100,arcade.color.GREEN)
    clouds(275+x,300,20)
    make_tree(150 + x,200,300)
    draw_house(400 + x,175+y,175)

    x += 4
    if x == 600:
        x = -600
        y+=20

arcade.schedule(draw_these,1/60)
arcade.run()