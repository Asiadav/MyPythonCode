import arcade
import random
import time
import math

SCREEN_WIDTH = 800#1120
SCREEN_HEIGHT = 600#630




        
class Enemy(arcade.Sprite):
    def __init__(self,x,y,image,scale):
        super().__init__(image)
        self.x = x
        self.y = y
        self.player_sprite = arcade.Sprite(image,scale)
        self.angle = 0
        
class Bullet(arcade.Sprite):
    def __init__(self,x,y,image,scale):
        super().__init__(image)
        self.x = x
        self.y = y
        self.player_sprite = arcade.Sprite(image,scale)
        self.angle = 0
        

class MyGame(arcade.Window):
      
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        
        self.set_mouse_visible(False)
        self.left_down = False
        self.start = True
        
        self.canMoveLeft = True
        self.canMoveRight = True
        self.canMoveDown = True
        self.canMoveUp = True
        
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.environment_list = arcade.SpriteList()
        
        
        
        self.player = arcade.Sprite("player.jpg",0.2)
        self.crosshair = arcade.Sprite("crosshair.png",0.1)   
        
        
        self.player_list.append(self.player)
        self.player_list.append(self.crosshair)      
        
        
    def setup(self):
        "make start screen and restart variables"
        
        self.player.center_x = SCREEN_WIDTH//2
        self.player.center_y = SCREEN_HEIGHT//2
        
        self.W_pressed = False
        self.A_pressed = False
        self.S_pressed = False
        self.D_pressed = False
        self.R_pressed = False    
        
        self.speed = 3
        
        self.player.changeX = 0
        self.player.changeY = 0
        
        self.bullet_speed = 13
        
        counter = 0
        placing_sprites = True
        
        while placing_sprites:
            counter += 2
            tree = arcade.Sprite("tree.png", .5)
            tree.center_x = random.randrange(30,SCREEN_WIDTH-30)
            tree.center_y = random.randrange(30,SCREEN_HEIGHT-30)
            self.environment_list.append(tree)
            
            crate = arcade.Sprite("crate.png", .1)
            crate.center_x = random.randrange(30,SCREEN_WIDTH-30)
            crate.center_y = random.randrange(30,SCREEN_HEIGHT-30)
            self.environment_list.append(crate)
            
            for item in self.environment_list:
                
                exception = self.environment_list.pop()
                no_no_list = arcade.check_for_collision_with_list(item,self.environment_list)
                for no_no in no_no_list:
                    no_no.kill()
                    counter -=1
                self.environment_list.append(exception)
                
            no_no_list = arcade.check_for_collision_with_list(self.player,self.environment_list)
            for no_no in no_no_list:
                no_no.kill()
                counter -= 1
            
            if counter >= 15:
                placing_sprites = False
            
        while not(self.start):
            "run start screen"
        
    def on_draw(self):
        arcade.start_render()
        
        self.player_list.draw()
        self.enemy_list.draw()
        self.bullet_list.draw()
        self.environment_list.draw()
        
        
        arcade.draw_triangle_filled(self.player.center_x, self.player.center_y + 30,self.player.center_x - 10, self.player.center_y + 40,self.player.center_x + 10, self.player.center_y + 40,arcade.color.RED)
    
        
    def update(self,dt):
        "move stuff"
            
        self.canMoveLeft = True
        self.canMoveRight = True
        self.canMoveDown = True
        self.canMoveUp = True        
        
        
        if self.W_pressed:
            self.player.changeY = self.speed
        if self.A_pressed: 
            self.player.changeX = -1 *self.speed
        if self.S_pressed:
            self.player.changeY = -1 *self.speed
        if self.D_pressed:
            self.player.changeX = self.speed
           
        for bullet in self.bullet_list:
            bullet.center_x += math.cos(math.radians(bullet.angle + 90)) * self.bullet_speed
            bullet.center_y += math.sin(math.radians(bullet.angle + 90)) * self.bullet_speed
                
            
        hit_list = arcade.check_for_collision_with_list(self.player,self.environment_list)
        
        for hit in hit_list:
            print("hit")
            if self.player.center_x > hit.center_x:
                #self.canMoveLeft = False
                self.player.center_x -= self.player.changeX
                
            if self.player.center_x < hit.center_x:
                #self.canMoveRight = False
                self.player.center_x -= self.player.changeX
                
            if self.player.center_y > hit.center_y:
                #self.canMoveDown = False
                self.player.center_y -= self.player.changeY
                
            if self.player.center_y < hit.center_y:
                #self.canMoveUp = False     
                self.player.center_y -= self.player.changeY
                
        self.player.center_x += self.player.changeX
        self.player.center_y += self.player.changeY

    def on_mouse_motion(self,x,y,dx,dy):
        
        self.mousePos_x = x
        self.mousePos_y = y
        
        self.crosshair.center_x = self.mousePos_x 
        self.crosshair.center_y = self.mousePos_y
        
        self.player.angle = math.degrees(math.atan2((self.player.center_y - self.crosshair.center_y),(self.player.center_x - self.crosshair.center_x))) -180
            
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        self.mouseClick_x = x
        self.mouseClick_y = y
        if button == arcade.MOUSE_BUTTON_LEFT:
            bullet = arcade.Sprite("bullet.png",.05)
            
            bullet.center_x = self.player.center_x - math.cos(math.radians(self.player.angle + 90)) * 12
            bullet.center_y = self.player.center_y - math.sin(math.radians(self.player.angle + 90)) * 12


            bullet.angle = math.degrees(math.atan2((bullet.center_y - self.crosshair.center_y),(bullet.center_x - self.crosshair.center_x))) + 90
            
          
            self.bullet_list.append(bullet)
            
            
    def on_key_press(self,key,modifiers):

        hit_list = arcade.check_for_collision_with_list(self.player,self.environment_list)
        
        for hit in hit_list:
            if self.player.center_x > hit.center_x:
                self.canMoveLeft = False
                
            if self.player.center_x < hit.center_x:
                self.canMoveRight = False
                
            if self.player.center_y > hit.center_y:
                self.canMoveDown = False
                
            if self.player.center_y < hit.center_y:
                self.canMoveUp = False  
                
                
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
            self.player.changeY = 0
        if key == arcade.key.A:
            self.A_pressed = False
            self.player.changeX = 0
            
        if key == arcade.key.S:
            self.S_pressed = False
            self.player.changeY = 0
            
        if key == arcade.key.D:
            self.D_pressed = False
            self.player.changeX = 0
            
        if key == arcade.key.R:
            self.R_pressed = False      
         

    
    
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT+40, "Drawing Example")
    window.setup()
    arcade.run()
        
main()