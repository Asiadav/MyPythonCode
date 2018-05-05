import arcade
import time
import random
import math

arcade.open_window(800, 800, "Test Window")
arcade.set_background_color((255,255,255))

def point_based_triangle(x, y, dist, color):
    x1 = x
    y1 = y+dist
    root3 = math.sqrt(3)
    x2 = x - (root3*(dist/2))
    y2 = y - dist/2
    x3 = x + (x - x2)
    y3 = y2

    arcade.draw_triangle_filled(x1,y1,x2,y2,x3,y3,color)
    '''
    arcade.draw_point(x,y,(200,200,200),10)
    arcade.draw_line(x,y,x1,y1,(0,0,0),2)
    arcade.draw_line(x,y,x2,y2,(0,0,0),2)
    arcade.draw_line(x,y,x3,y3,(0,0,0),2)
    '''

#point_based_triangle(400,400,300,(100,100,100))

def make_tree(x,y,size):
    height = size/2
    width = size/5
    x1 = x
    y1 = y - 3*height/4


    arcade.draw_rectangle_filled(x1,y1,width,height/2,(200,150,100))

    point_based_triangle(x,y-2*width/3,size/3,arcade.color.FOREST_GREEN)

    point_based_triangle(x,y+height/16,size/4,arcade.color.FOREST_GREEN)





while True:
    arcade.start_render()
    for i in range (40):
        make_tree(random.randint(10,790),random.randint(10,790),random.randint(50,100))
    arcade.finish_render()
    time.sleep(.1)


arcade.run()