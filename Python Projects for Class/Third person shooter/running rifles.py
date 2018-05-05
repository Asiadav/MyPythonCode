import arcade
import random
import time

SCREEN_WIDTH = int(640)
SCREEN_HEIGHT = int(480)



class MyGame(arcade.Window):
      
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_BLUE)
        
        self.set_mouse_visible(True)
        self.left_down = False
        self.start = False
        
    def setup(self):
        "make start screen and restart variables"
    
    
    
    
        self.start = True
        
    def on_draw(self):
        arcade.start_render()
        
    def update(self,dt):
        "move stuff"

    def on_mouse_motion(self,x,y,dx,dy):
        
        if x < SCREEN_WIDTH - 20 and x > 20 :
            self.player_sprite.center_x = x
        
        if y < SCREEN_HEIGHT - 25 and y > 25 :
            self.player_sprite.center_y = y
            
        if 40 < x < 60 and 40 < y < 60:
            self.mouse = 1
            
        
    def on_key_press(self,key,modifiers):
        
        if self.start:
            if key == arcade.key.W:
                self.easy = False
            if key == arcade.key.A:
                self.easy = True
            if key == arcade.key.S:
                self.easy = False
            if key == arcade.key.D:
                self.easy = True
            
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.left_down = True
    
    
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT+40, "Drawing Example")
    window.setup()
    arcade.run()
        
main()