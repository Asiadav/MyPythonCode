""" how to do a class"""

import arcade
import random

class Ball:
    
    def __init__(self,x,y,size,color):
        self.x = x
        self.y = x
        self.size = size
        self.color = color
        
    def draw(self):
        arcade.draw_circle_filled(self.x,self.y,self.size,self.color)
        
    def update(self):

        if self.x < self.size:
            self.dx = self.dx * -1
            
        if self.x > 640 - self.size:
            self.dx = self.dx * -1
            
        if self.y < self.size:
            self.dy = self.dy * -1
            
        if self.y > 480 - self.size:
            self.dy = self.dy * -1 

       # print(self.y)
       # print(self.dy)
        
    
class MyGame(arcade.Window):
      
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.ball_list = []
        
        self.set_mouse_visible(False)
        
        x = 50
        y = 50
        self.size = 20
        color = (200,100,50)
        self.cord_list_x = []
        self.cord_list_y = []
        
        self.ball = Ball(random.randint(50,500),random.randint(50,400),self.size,arcade.color.RED)


        
        
    def on_draw(self):
        
        arcade.start_render()
        for x in range(len(self.cord_list_x)):
            arcade.draw_circle_filled(self.cord_list_x[x], self.cord_list_y[x], self.size, arcade.color.RED)        
        self.ball.draw()
        


    def on_mouse_motion(self,x,y,dx,dy):
        self.ball.x = x
        self.ball.y = y
        
    def on_mouse_press(self,x,y,button,modifiers):
        if button ==arcade.MOUSE_BUTTON_LEFT:
            self.cord_list_x.append(x)
            self.cord_list_y.append(y)
        

def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()
        
main()