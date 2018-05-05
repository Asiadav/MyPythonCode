import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


global x
global y
x = 400
y = 100
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
arcade.set_background_color(arcade.color.DARK_BLUE)

def drawGround():
    # Draw the ground
    arcade.draw_rectangle_filled(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,arcade.color.DARK_BLUE)
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

def on_draw(delta_time):
    """"draw everything"""
    arcade.start_render()

on_draw.snow_person1_x = 150


def drawSnowPerson(x,y):
    # Draw a snow person

    # Snow
    arcade.draw_circle_filled(x, 200 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 280 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 340+  y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(15 + x, 350+y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(-15 +x, 350+y, 5, arcade.color.BLACK)

    # Nose
    arcade.draw_triangle_filled(-40 + x,340+y,x,330+y,x,340+y,arcade.color.ORANGE)
def main(time):
    global x
    global y

    x = x + random.randint(-5,5)
    y = y + random.randint(-5,5)

    drawGround()

    drawSnowPerson(x,y)


#  Finish and run


arcade.schedule(main, 1/60)
arcade.run()