import arcade
import time
import random
import math
import winsound

arcade.open_window(500, 500, "Clock")
arcade.set_background_color((255,255,255))

global seconds
global smallAngle
global bigAngle
global x1
global x2
global x3
global y1
global y2
global y3
global length
global width

seconds = 90
smallAngle = 90
bigAngle = 90
x1 = 0
y1 = 0
x2 = 0
y2 = 0
length = 150
width = 8

def scare():

    name = 'creepy boi.png'
    texture = arcade.load_texture(name)
    arcade.draw_texture_rectangle(255, 240, 600, 250, texture)
    winsound.PlaySound('creepy sound.wav',winsound.SND_FILENAME)




def run(time):
    global seconds
    global smallAngle
    global bigAngle
    global x1
    global x2
    global x3
    global y1
    global y2
    global y3
    global length
    global width

    if bigAngle == 0:
        bigAngle = 360
    if smallAngle == 0:
        smallAngle = 360
    if seconds == 0:
        seconds = 360

    radSecondsBig = math.pi * bigAngle / 180
    radSecondsSmall = math.pi * smallAngle / 180
    radSeconds = math.pi * seconds / 180

    x1 = 45 * math.cos(radSecondsBig) + 250
    x2 = 20 * math.cos(radSecondsSmall) + 250
    x3 = 55 * math.cos(radSeconds) + 250
    y1 = 45 * math.sin(radSecondsBig) + 250
    y2 = 20 * math.sin(radSecondsSmall) + 250
    y3 = 55 * math.sin(radSeconds) + 250


    arcade.draw_circle_filled(250,250,210,(130,100,50))
    arcade.draw_circle_filled(250,250,200,(65,50,25))
    arcade.draw_circle_filled(250,250,180,(205,150,100))

    arcade.draw_circle_filled(190, 300, 40, (250,250,250))
    arcade.draw_circle_filled(310, 300, 40, (250,250,250))
    arcade.draw_circle_filled(200, 300, 20, (0,0,0))
    arcade.draw_circle_filled(300, 300, 20, (0,0,0))

    arcade.draw_circle_filled(250,210,50,(250,250,250))
    arcade.draw_circle_filled(250,225,50,(205,150,100))

    if random.randint(1,100) > 93:
        arcade.draw_circle_filled(190,320,50,(205,150,100))


    arcade.draw_text("12",220,380,(0,0,0),50)
    arcade.draw_text("11",140,350,(0,0,0),50)
    arcade.draw_text("10",85,290,(0,0,0),50)
    arcade.draw_text("9",80,220,(0,0,0),50)
    arcade.draw_text("8",100,145,(0,0,0),50)
    arcade.draw_text("7",160,95,(0,0,0),50)
    arcade.draw_text("6",230,75,(0,0,0),50)
    arcade.draw_text("5",300,95,(0,0,0),50)
    arcade.draw_text("4",360,140,(0,0,0),50)
    arcade.draw_text("3",390,220,(0,0,0),50)
    arcade.draw_text("2",370,300,(0,0,0),50)
    arcade.draw_text("1",320,355,(0,0,0),50)

    arcade.draw_rectangle_filled(x2,y2,length/1.5,width*1.4,(50,50,50),smallAngle)
    arcade.draw_rectangle_filled(x1,y1,length/1.2,width,(100,100,100),bigAngle)
    arcade.draw_rectangle_filled(x3,y3,length*1.05,width*0.6,(150,150,150),seconds)

    arcade.draw_circle_filled(250,250,10,(50,40,20))
    if random.randint(1,100) > 97:
        #arcade.open_window(2000, 1000, "")
        arcade.set_background_color((255,255,255))
        scare()
        'you cannot handle this feature'
    bigAngle -= 1/10
    smallAngle -= 1/120
    seconds -= 6
    winsound.PlaySound('tick.wav',winsound.SND_FILENAME)

arcade.start_render()
arcade.schedule(run,1/60)
arcade.run()