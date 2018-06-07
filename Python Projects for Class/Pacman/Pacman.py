import arcade
import random
import time
import math
import winsound
import os

SCREEN_WIDTH = 1120
SCREEN_HEIGHT = 630


class MyGame(arcade.Window):
      
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        
        
        """Sprite Inits"""
        self.wall_list = arcade.SpriteList()
        self.dot_list = arcade.SpriteList()
        self.powerPellet_list = arcade.SpriteList()
        
        self.pacman = arcade.Sprite("pacman.png",0.5)
        self.inky = arcade.Sprite("inky.png",0.5)
        self.blinky = arcade.Sprite("blinky.jpg",0.5)
        self.pinky = arcade.Sprite("pinky.png",0.5)
        self.chlyde = arcade.Sprite("chlyde.png",0.4)
        
    def setup(self):
        "make start screen and restart variables"
        
        
        

 
            
    def on_draw(self):
        
        arcade.start_render()        
        
        self.pacman.draw()
        self.wall_list.draw()
        self.dot_list.draw()
        self.powerPellet_list.draw()
        self.inky.draw()
        self.blinky.draw()
        self.pinky.draw()
        self.chlyde.draw()
        
        

    def enemy_action(self):
        "what the enemy does" 
        
     
    def update(self,dt):
        "move stuff"
    
            
    def on_key_press(self,key,modifiers):

                
        if key == arcade.key.W and self.canMoveUp:
            self.W_pressed = True
        if key == arcade.key.A and self.canMoveLeft:
            self.A_pressed = True
        if key == arcade.key.S and self.canMoveDown:
            self.S_pressed = True
        if key == arcade.key.D and self.canMoveRight:
            self.D_pressed = True
        if key == arcade.key.R:
            self.R_pressed = True
            
    def on_key_release(self,key,modifiers):
        
        if key == arcade.key.W:
            self.W_pressed = False

        if key == arcade.key.A:
            self.A_pressed = False
        
        if key == arcade.key.S:
            self.S_pressed = False
            
        if key == arcade.key.D:
            self.D_pressed = False
            
        if key == arcade.key.R:
            self.R_pressed = False      
        
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT+40, "PacMan")
    window.setup()
    arcade.run()
        
main()