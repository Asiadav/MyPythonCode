

def ball_sim():
    global stop
    stop = 0
    
    import arcade
    import math
    import random
    import os
    
    
    global xv
    global yv
    global x
    global y
    global width
    global height
    global csize
    global run0
    run0 = 0
    xv = random.randint(-10,10)
    yv = random.randint(-10,10)
    
    x = random.randint(50,550)
    y = random.randint(150,350)
    
    csize = 20
    
    width = 600
    height = 400
    
    
    global xv1
    global yv1
    global x1
    global y1
    global csize1
    global run1
    run1 = 0
    
    xv1 = random.randint(-10,10)
    yv1 = random.randint(-10,10)
    
    x1 = random.randint(50,550)
    y1 = random.randint(150,350)
    
    csize1 = 20
    
    
    
    arcade.open_window(width,height, "Gravity Simulation")
    arcade.set_background_color(arcade.color.BLUE)
    
    def collision_detect():
        global x
        global y
        global x1
        global y1
        global xv
        global yv
        global xv1
        global yv1
    
        xdist = (x - x1)**2
        ydist = (y - y1)**2
        dist = math.sqrt((x-x1)**2+(y-y1)**2)
        if dist <= csize*2:
            if dist == csize:
                if xv < 0:
                    xv += csize
                if xv > 0:
                    xv -= csize
    
                if yv < 0:
                    yv += csize
                if yv > 0:
                    yv -= csize
    
                if xv1 < 0:
                    xv1 += csize
                if xv1 > 0:
                    xv1 -= csize
    
                if yv1 < 0:
                    yv1 += csize
                if yv1 > 0:
                    yv1 -= csize
    
                #print("fixed")
            #print("hit",dist)
            return 1
    
    def gravity_ball():
        global xv
        global yv
        global x
        global y
        global width
        global height
        global csize
        global xv1
        global yv1
        global x1
        global y1
        global stop 
        
        if x > width - csize:
            xv = (-1 * xv) * .9
            x += xv
            if x < csize:
                x = csize
        if y > height-csize:
            yv = (-1 * yv) * .9
            y += yv
            if y < csize:
                y = csize
    
        if x < csize:
            xv = (-1 * xv) * .9
            x += xv
            if x < csize:
                x = csize
        if y < csize:
            yv = (-1 * yv) * .9
            y += yv
            if y < csize:
                y = csize
    
    
        if collision_detect() == 1:
            yv = (-1 * yv) * .9
            xv = (-1 * xv) * .9
    
            yv1 = (-1 * yv1) * .9
            xv1 = (-1 * xv1) * .9
            '''
            if yv < 0:
                yv = -1 * yv
            if yv1 < 0:
                yv1 = -1 * yv1
            if xv < 0:
                xv = -1 * xv
            if xv1 < 0:
                xv1 = -1 * xv1
            '''
            y += yv
            x += xv
    
            y1 += yv1
            x1 += xv1
    
        if y > csize:
            yv -= 1
    
    
        x += xv
        y += yv
    
        if 0 < yv < 0.5:
            yv = 0
            stop += 1
            print(stop)
        if 0 > yv > -0.5:
            yv = 0
            stop += 1
            print(stop)
    
        if xv < 0:
            xv += 0.01
        if xv > 0:
            xv -= 0.01
    
        if 0 < xv < 0.01:
            xv = 0
            stop += 1
            print(stop)
        if 0 > xv > -0.01:
            xv = 0
            stop += 1
            print(stop)
        #print("delta",xv)
        #print("y",y)
        #print("x",x)
    
        arcade.draw_circle_filled(x,y,csize,arcade.color.RED)
    
    def gravity_ball2():
        global xv1
        global yv1
        global x1
        global y1
        global csize1
        global height
        global width
        global stop 
        
        if x1 > width - csize:
            xv1 = (-1 * xv1) * .9
            x1 += xv1
            if x1 < csize1:
                x1 = csize1
        if y1 > height-csize1:
            yv1 = (-1 * yv1) * .9
            y1 += yv1
            if y1 < csize1:
                y1 = csize1
    
        if x1 < csize1:
            xv1 = (-1 * xv1) * .9
            x1 += xv1
            if x1 < csize1:
                x1 = csize1
        if y1 < csize1:
            yv1 = (-1 * yv1) * .9
            y1 += yv1
            if y1 < csize1:
                y1 = csize1
    
        if y1 > csize1:
            yv1 -= 1
    
    
        x1 += xv1
        y1 += yv1
    
        if 0 < yv1 < 0.5:
            yv1 = 0
            stop += 1
            print(stop)
        if 0 > yv1 > -0.5:
            yv1 = 0
            stop += 1
            print(stop)
    
        if xv1 < 0:
            xv1 += 0.01
        if xv1 > 0:
            xv1 -= 0.01
    
        if 0 < xv1 < 0.01:
            xv1 = 0
            stop += 1
            print(stop)
        if 0 > xv1 > -0.01:
            xv1 = 0
            stop += 1
            print(stop)
        #print("delta",xv)
        #print("y",y)
        #print("x",x)
    
    
        arcade.draw_circle_filled(x1,y1,csize1,arcade.color.GREEN)
    def run(time):
        global xv
        global yv
        global x
        global y
        global width
        global height
        global csize
    
        global xv1
        global yv1
        global x1
        global y1
        global csize1
        global stop
        
        if stop >= 42:
            arcade.close_window
            ball_sim()

        arcade.start_render()
    
        gravity_ball()
        gravity_ball2()
        
    arcade.schedule(run,1/60)
    arcade.run()
    
ball_sim()