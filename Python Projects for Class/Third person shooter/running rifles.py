import arcade
import random
import time
import math
import winsound
import os

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
        
        self.sfx = False
    
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()
        self.tree_list = arcade.SpriteList()
        self.crate_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        
        for i in range(2):
            
            background = arcade.Sprite("background.jpg")
            background.center_y = i * SCREEN_HEIGHT/3 
            self.background_list.append(background)
            
        
        self.player = arcade.Sprite("player.png",0.2)
        self.crosshair = arcade.Sprite("crosshair.png",0.1)   
        self.enemy = arcade.Sprite("player.png", 0.2)
        
        
        self.enemy_list.append(self.enemy)
        
        self.player_list.append(self.player)
        self.player_list.append(self.crosshair)      
        
        
    def setup(self):
        "make start screen and restart variables"
        
        self.player.center_x = 20
        self.player.center_y = 20
        
        self.enemy.center_x = SCREEN_WIDTH - 20
        self.enemy.center_y = SCREEN_HEIGHT - 20
        
        self.W_pressed = False
        self.A_pressed = False
        self.S_pressed = False
        self.D_pressed = False
        self.R_pressed = False    
        
        self.player.prevAngle = 0
        
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
            self.tree_list.append(tree)
            
            for item in self.tree_list:
                
                exception = self.tree_list.pop()
                no_no_list = arcade.check_for_collision_with_list(item,self.tree_list)
                for no_no in no_no_list:
                    no_no.kill()
                    counter -=1
                self.tree_list.append(exception)

       
            crate = arcade.Sprite("crate.png", .1)
            crate.center_x = random.randrange(30,SCREEN_WIDTH-30)
            crate.center_y = random.randrange(30,SCREEN_HEIGHT-30)
            self.crate_list.append(crate)
            
            for item in self.crate_list:
                
                exception = self.crate_list.pop()
                no_no_list = arcade.check_for_collision_with_list(item,self.crate_list)
                for no_no in no_no_list:
                    no_no.kill()
                    counter -=1
                self.crate_list.append(exception)
            
            for item in self.crate_list:
                
                exception = self.crate_list.pop()
                no_no_list = arcade.check_for_collision_with_list(item,self.tree_list)
                for no_no in no_no_list:
                    no_no.kill()
                    counter -=1
                self.crate_list.append(exception)
                
            no_no_list = arcade.check_for_collision_with_list(self.player,self.tree_list)
            for no_no in no_no_list:
                no_no.kill()
                counter -= 1
                
            no_no_list = arcade.check_for_collision_with_list(self.player,self.crate_list)
            for no_no in no_no_list:
                no_no.kill()
                counter -= 1
            
            if counter >= 20:
                placing_sprites = False
        if not(self.sfx):
            playlist = ["danger.wav","waveshaper.wav"]
            selection = playlist[random.randint(0,len(playlist)-1)]
            winsound.PlaySound(selection, winsound.SND_ASYNC)

        while not(self.start):
            "run start screen"
        
    def on_draw(self):
        arcade.start_render()        
        
        self.background_list.draw()
        
        
        self.player_list.draw(),
        self.enemy_list.draw()
        self.bullet_list.draw()
        self.tree_list.draw()
        self.crate_list.draw()
        
        arcade.draw_triangle_filled(self.player.center_x, self.player.center_y + 30,self.player.center_x - 10, self.player.center_y + 40,self.player.center_x + 10, self.player.center_y + 40,arcade.color.RED)
        
        arcade.draw_rectangle_filled(SCREEN_WIDTH//2,SCREEN_HEIGHT+20,SCREEN_WIDTH,40,arcade.color.WHITE)
        
    def enemy_action(self):
        "what the enemy does"
        
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
            tree_hit_list = arcade.check_for_collision_with_list(bullet,self.tree_list)
            crate_hit_list = arcade.check_for_collision_with_list(bullet,self.crate_list)
            enemy_hit_list = arcade.check_for_collision_with_list(bullet,self.enemy_list)
            if len(tree_hit_list) > 0:
                bullet.kill()
            if len(crate_hit_list) > 0:
                bullet.kill()
            if len(enemy_hit_list) > 0:
                bullet.kill()
                
        for bullet in self.enemy_bullet_list:
            bullet.center_x += math.cos(math.radians(bullet.angle + 90)) * self.bullet_speed
            bullet.center_y += math.sin(math.radians(bullet.angle + 90)) * self.bullet_speed
            tree_hit_list = arcade.check_for_collision_with_list(bullet,self.tree_list)
            crate_hit_list = arcade.check_for_collision_with_list(bullet,self.crate_list)
            player_hit_list = arcade.check_for_collision_with_list(bullet,self.player_list)
            if len(tree_hit_list) > 0:
                bullet.kill()
            if len(crate_hit_list) > 0:
                bullet.kill()
            if len(player_hit_list) > 0:
                bullet.kill()
                
        self.player.center_x += self.player.changeX 
        crate_hit_list = arcade.check_for_collision_with_list(self.player,self.crate_list)
        tree_hit_list = arcade.check_for_collision_with_list(self.player,self.tree_list)
        if len(crate_hit_list) != 0 or len(tree_hit_list) != 0:
            self.canTurn = False
            self.player.center_x -= self.player.changeX 
        
        self.player.center_y += self.player.changeY
        crate_hit_list = arcade.check_for_collision_with_list(self.player,self.crate_list)
        tree_hit_list = arcade.check_for_collision_with_list(self.player,self.tree_list)
        if len(crate_hit_list) != 0 or len(tree_hit_list) != 0:
            self.canTurn = False
            self.player.center_y -= self.player.changeY       
    
        if self.player.center_x < 15 or self.player.center_x > SCREEN_WIDTH-15:
            self.player.center_x -= self.player.changeX
        if self.player.center_y < 15 or self.player.center_y > SCREEN_HEIGHT-25:
            self.player.center_y -= self.player.changeY
            
    def on_mouse_motion(self,x,y,dx,dy):
        
        self.mousePos_x = x
        self.mousePos_y = y
        
        
        self.crosshair.center_x = self.mousePos_x 
        self.crosshair.center_y = self.mousePos_y
        
    
        self.player.angle = math.degrees(math.atan2((self.player.center_y - self.crosshair.center_y),(self.player.center_x - self.crosshair.center_x))) -180
                crate_hit_list = arcade.check_for_collision_with_list(self.player,self.crate_list)
        tree_hit_list = arcade.check_for_collision_with_list(self.player,self.tree_list)
        if len(crate_hit_list) != 0 or len(tree_hit_list) != 0:
            if -360<self.player.angle<-315 or -45<self.player.angle<0:
                self.player.center_x -= self.speed
                
                crate_hit_list = arcade.check_for_collision_with_list(self.player,self.crate_list)
                tree_hit_list = arcade.check_for_collision_with_list(self.player,self.tree_list)
                if len(crate_hit_list) != 0 or len(tree_hit_list) != 0:
                    self.player.center_x += self.speed     
                    
            if -315<self.player.angle<-225:
                self.player.center_y -= self.speed
                
                crate_hit_list = arcade.check_for_collision_with_list(self.player,self.crate_list)
                tree_hit_list = arcade.check_for_collision_with_list(self.player,self.tree_list)
                if len(crate_hit_list) != 0 or len(tree_hit_list) != 0:
                    self.player.center_y += self.speed        
                    
            if -225<self.player.angle<-135:
                self.player.center_x += self.speed
                
                crate_hit_list = arcade.check_for_collision_with_list(self.player,self.crate_list)
                tree_hit_list = arcade.check_for_collision_with_list(self.player,self.tree_list)
                if len(crate_hit_list) != 0 or len(tree_hit_list) != 0:
                    self.player.center_x -= self.speed        
                    
            if -135<self.player.angle<-45:
                self.player.center_y += self.speed
                
                crate_hit_list = arcade.check_for_collision_with_list(self.player,self.crate_list)
                tree_hit_list = arcade.check_for_collision_with_list(self.player,self.tree_list)
                if len(crate_hit_list) != 0 or len(tree_hit_list) != 0:
                    self.player.center_y -= self.speed        
                    
            print(self.player.angle)
                
            self.player.angle = self.player.prevAngle   
            
        else:
            self.player.angle = math.degrees(math.atan2((self.player.center_y - self.crosshair.center_y),(self.player.center_x - self.crosshair.center_x))) -180
            self.player.prevAngle = self.player.angle
            print(self.player.angle)
            
          
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        self.mouseClick_x = x
        self.mouseClick_y = y
        if button == arcade.MOUSE_BUTTON_LEFT:
            bullet = arcade.Sprite("bullet.png",.05)
            
            if self.sfx:
                winsound.PlaySound("shot1.wav", winsound.SND_ASYNC)
            
            bullet.center_x = self.player.center_x - math.cos(math.radians(self.player.angle + 90)) * 12
            bullet.center_y = self.player.center_y - math.sin(math.radians(self.player.angle + 90)) * 12


            bullet.angle = self.player.angle - 90 #math.degrees(math.atan2((bullet.center_y - self.crosshair.center_y),(bullet.center_x - self.crosshair.center_x))) + 90
            
          
            self.bullet_list.append(bullet)
            
            
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