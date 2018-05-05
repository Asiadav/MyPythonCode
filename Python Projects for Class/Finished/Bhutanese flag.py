import arcade
import time
import random

windowX = 200
windowY = 100


arcade.open_window(windowX, windowY, "Bhutanese flag")

arcade.set_background_color((255,255,255))

arcade.start_render()

arcade.draw_rectangle_filled(windowX/2,windowY/4,windowX,windowY/2,(0,180,0))

arcade.draw_rectangle_filled(windowX/2,4*windowY/9,7*windowX/12,5*windowY/18,arcade.color.RED)      #body

arcade.draw_rectangle_filled(4*windowX/15,25*windowY/36,windowX/10,windowY/4,arcade.color.RED)      #neck

arcade.draw_rectangle_filled(29*windowX/120,20*windowY/72,8*windowX/120,28*windowY/72,arcade.color.RED)       #legs
arcade.draw_rectangle_filled(windowX/2,20*windowY/72,8*windowX/120,28*windowY/72,arcade.color.RED)
arcade.draw_rectangle_filled(3*windowX/4,20*windowY/72,8*windowX/120,28*windowY/72,arcade.color.RED)
arcade.draw_rectangle_filled(18*windowX/120,35*windowY/72,8*windowX/120,28*windowY/72,arcade.color.RED, 35)

arcade.draw_rectangle_filled(24*windowX/120,8*windowY/72,12*windowX/120,6*windowY/72,arcade.color.RED)       #feet
arcade.draw_rectangle_filled(55*windowX/120,8*windowY/72,12*windowX/120,6*windowY/72,arcade.color.RED)
arcade.draw_rectangle_filled(85*windowX/120,8*windowY/72,12*windowX/120,6*windowY/72,arcade.color.RED)
arcade.draw_rectangle_filled(12*windowX/120,45*windowY/72,12*windowX/120,6*windowY/72,arcade.color.RED, 35)

arcade.draw_circle_filled(windowX/4,55*windowY/72,(10*(windowX+windowY)/192),arcade.color.RED)            #head

arcade.draw_rectangle_filled(100*windowX/120,45*windowY/72,8*windowX/120,28*windowY/72,arcade.color.RED, 150) #tail
arcade.draw_triangle_filled(110*windowX/120,70*windowY/72,110*windowX/120,55*windowY/72,100*windowX/120,55*windowY/72,arcade.color.RED)

arcade.draw_rectangle_filled(50*windowX/120,50*windowY/72,8*windowX/120,28*windowY/72,arcade.color.RED)       #wing
arcade.draw_rectangle_filled(65*windowX/120,55*windowY/72,40*windowX/120,20*windowY/72,arcade.color.RED)

arcade.draw_triangle_filled(28*windowX/120,55*windowY/72,8*windowX/120,55*windowY/72,20*windowX/120,50*windowY/72,arcade.color.RED)

arcade.draw_point(27*windowX/120,57*windowY/72,(0,0,0),4)


arcade.finish_render()


for i in range(100):
    windowX = random.randint(50,1000)
    windowY = random.randint(30,600)
    arcade.open_window(windowX, windowY, "Bhutanese flag")

    arcade.set_background_color((255,255,255))

    arcade.start_render()

    arcade.draw_rectangle_filled(windowX/2,windowY/4,windowX,windowY/2,(0,180,0))

    arcade.draw_rectangle_filled(windowX/2,4*windowY/9,7*windowX/12,5*windowY/18,arcade.color.RED)      #body

    arcade.draw_rectangle_filled(4*windowX/15,25*windowY/36,windowX/10,windowY/4,arcade.color.RED)      #neck

    arcade.draw_rectangle_filled(29*windowX/120,20*windowY/72,8*windowX/120,28*windowY/72,arcade.color.RED)       #legs
    arcade.draw_rectangle_filled(windowX/2,20*windowY/72,8*windowX/120,28*windowY/72,arcade.color.RED)
    arcade.draw_rectangle_filled(3*windowX/4,20*windowY/72,8*windowX/120,28*windowY/72,arcade.color.RED)
    arcade.draw_rectangle_filled(18*windowX/120,35*windowY/72,8*windowX/120,28*windowY/72,arcade.color.RED, 35)

    arcade.draw_rectangle_filled(24*windowX/120,8*windowY/72,12*windowX/120,6*windowY/72,arcade.color.RED)       #feet
    arcade.draw_rectangle_filled(55*windowX/120,8*windowY/72,12*windowX/120,6*windowY/72,arcade.color.RED)
    arcade.draw_rectangle_filled(85*windowX/120,8*windowY/72,12*windowX/120,6*windowY/72,arcade.color.RED)
    arcade.draw_rectangle_filled(12*windowX/120,45*windowY/72,12*windowX/120,6*windowY/72,arcade.color.RED, 35)

    arcade.draw_circle_filled(windowX/4,55*windowY/72,(10*(windowX+windowY)/192),arcade.color.RED)            #head

    arcade.draw_rectangle_filled(100*windowX/120,45*windowY/72,8*windowX/120,28*windowY/72,arcade.color.RED, 150) #tail
    arcade.draw_triangle_filled(110*windowX/120,70*windowY/72,110*windowX/120,55*windowY/72,100*windowX/120,55*windowY/72,arcade.color.RED)

    arcade.draw_rectangle_filled(50*windowX/120,50*windowY/72,8*windowX/120,28*windowY/72,arcade.color.RED)       #wing
    arcade.draw_rectangle_filled(65*windowX/120,55*windowY/72,40*windowX/120,20*windowY/72,arcade.color.RED)

    arcade.draw_triangle_filled(28*windowX/120,55*windowY/72,8*windowX/120,55*windowY/72,20*windowX/120,50*windowY/72,arcade.color.RED)

    arcade.draw_point(27*windowX/120,57*windowY/72,(0,0,0),4*(windowX+windowY)/192)


    arcade.finish_render()
    time.sleep(.5)

arcade.run()

