import arcade
import random
import time
import math
import winsound
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Player(arcade.AnimatedWalkingSprite):
    
    def __init__(self,x,y):
        super().__init__(self)
        self.center_x = x
        self.center_y = y
        self.scale = 1.0
        
        self.stand_right_textures = []
        self.stand_right_textures.append(arcade.load_texture("snake_stand_7.png"))
        
        self.walk_right_textures = []
        self.walk_right_textures.append(arcade.load_texture("snake_run_0.png"))
        self.walk_right_textures.append(arcade.load_texture("snake_run_1.png"))
        self.walk_right_textures.append(arcade.load_texture("snake_run_2.png"))
        self.walk_right_textures.append(arcade.load_texture("snake_run_3.png"))
        self.walk_right_textures.append(arcade.load_texture("snake_run_5.png"))
        self.walk_right_textures.append(arcade.load_texture("snake_run_4.png"))
        self.walk_right_textures.append(arcade.load_texture("snake_run_8.png"))
        self.walk_right_textures.append(arcade.load_texture("snake_run_9.png"))   
        self.walk_right_textures.append(arcade.load_texture("snake_run_8.png"))
        
        self.walk_right_textures_gun = []
        self.walk_right_textures_gun.append(arcade.load_texture("snake_run_gun_0.png"))
        self.walk_right_textures_gun.append(arcade.load_texture("snake_run_gun_1.png"))
        self.walk_right_textures_gun.append(arcade.load_texture("snake_run_gun_2.png"))
        self.walk_right_textures_gun.append(arcade.load_texture("snake_run_gun_3.png"))
        self.walk_right_textures_gun.append(arcade.load_texture("snake_run_gun_5.png"))
        self.walk_right_textures_gun.append(arcade.load_texture("snake_run_gun_4.png"))
        self.walk_right_textures_gun.append(arcade.load_texture("snake_run_gun_8.png"))
        self.walk_right_textures_gun.append(arcade.load_texture("snake_run_gun_9.png"))   
        self.walk_right_textures_gun.append(arcade.load_texture("snake_run_gun_8.png"))        
        
        self.stand_left_textures = []
        self.stand_left_textures.append(arcade.load_texture("snake_stand_7.png", mirrored = True))
        
        self.walk_left_textures = []
        self.walk_left_textures.append(arcade.load_texture("snake_run_0.png", mirrored = True))
        self.walk_left_textures.append(arcade.load_texture("snake_run_1.png", mirrored = True))
        self.walk_left_textures.append(arcade.load_texture("snake_run_2.png", mirrored = True))
        self.walk_left_textures.append(arcade.load_texture("snake_run_3.png", mirrored = True))
        self.walk_left_textures.append(arcade.load_texture("snake_run_5.png", mirrored = True))
        self.walk_left_textures.append(arcade.load_texture("snake_run_4.png", mirrored = True))     
        self.walk_left_textures.append(arcade.load_texture("snake_run_8.png", mirrored = True))
        self.walk_left_textures.append(arcade.load_texture("snake_run_9.png", mirrored = True))  
        self.walk_left_textures.append(arcade.load_texture("snake_run_8.png", mirrored = True))
        
        #self.walk_up_textures = []
        #self.walk_up_textures.append(arcade.load_texture("snake_jump_0.png"))
        
        self.walk_up_textures_left = []
        self.walk_up_textures_left.append(arcade.load_texture("snake_jump_0.png", mirrored = True))
        
        self.texture_change_distance = 20     
'''
class Enemy(arcade.AnimatedTimeSprite):
    def __init__(self, x, y):
        super().__init__(self)
        self.center_x = x
        self.center_y = y
        self.scale = 0.5        
'''    
        
        
class Ring(arcade.AnimatedTimeSprite):
    def __init__(self,x,y):
        super().__init__(self)
        self.center_x = x
        self.center_y = y
        self.scale = .75
    
        self.textures = []
        self.textures.append(arcade.load_texture("ring_1.png"))
        self.textures.append(arcade.load_texture("ring_2.png"))
        self.textures.append(arcade.load_texture("ring_3.png"))
        self.textures.append(arcade.load_texture("ring_4.png"))
              
        
        
class MyGame(arcade.Window):
      
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        
        
        """Sprite Inits"""
                
        self.background = arcade.Sprite("background.png",1.95)
        self.background.center_x = SCREEN_WIDTH 
        self.background.center_y = SCREEN_HEIGHT//2
        
        self.player_list = arcade.SpriteList()
        self.player = Player(SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
        self.player.update_animation()
        
        self.block_list = arcade.SpriteList() 
        self.ring_list = arcade.SpriteList()
        self.spike_list = arcade.SpriteList()
        
        
        self.floor = arcade.Sprite("floor.png", .4)
        self.floor.center_x = 640
        self.floor.center_y = 20
        self.ceiling = arcade.Sprite("floor.png", .4)
        self.ceiling.center_x = 640
        self.ceiling.center_y = SCREEN_HEIGHT - 20     
        
        self.floor2 = arcade.Sprite("floor.png", .4)
        self.floor2.center_x = 1280
        self.floor2.center_y = 20
        self.ceiling2 = arcade.Sprite("floor.png", .4)
        self.ceiling2.center_x = 1280
        self.ceiling2.center_y = SCREEN_HEIGHT - 20        
        
        self.floor3 = arcade.Sprite("floor.png", .4)
        self.floor3.center_x = 1280 + 640
        self.floor3.center_y = 20
        self.ceiling3 = arcade.Sprite("floor.png", .4)
        self.ceiling3.center_x = 1280 + 640
        self.ceiling3.center_y = SCREEN_HEIGHT - 20        
        
        self.wall = arcade.Sprite("floor.png", .4)
        self.wall.angle = 90
        self.wall.center_x = 20
        self.wall.center_y = SCREEN_HEIGHT//2 - 360       
        self.wall2 = arcade.Sprite("floor.png", .4)
        self.wall2.angle = 90
        self.wall2.center_x = 1280 + 1280
        self.wall2.center_y = SCREEN_HEIGHT//2 - 340       
        
        self.block_list.append(self.floor)
        self.block_list.append(self.ceiling)
        self.block_list.append(self.floor2)
        self.block_list.append(self.ceiling2) 
        self.block_list.append(self.floor3)
        self.block_list.append(self.ceiling3)
        self.block_list.append(self.wall)
        self.block_list.append(self.wall2)
        
        ring_coords = [(60,200),(65,535)]        
        for coord in ring_coords:
            ring = Ring(coord[0],coord[1])           
            self.ring_list.append(ring)
        
        spike_coords = [(450,250,90)]        
        for coord in spike_coords:
            spikes = arcade.Sprite("spikes.png",.25)
            spikes.angle = coord[2]
            spikes.center_x = coord[0]
            spikes.center_y = coord[1]
            self.spike_list.append(spikes)        
            
        block_coords = [(60,240),(70,460),(100,200),(120,330),(130,200),(400,350)]        
        for coord in block_coords:
            block = arcade.Sprite("block.png",.5)
            block.center_x = coord[0]
            block.center_y = coord[1]
            self.block_list.append(block)
        plat_coords = [(170,362),(410,160),(530,250),(750,450),(900,350)]        
        for coord in plat_coords:
            plat = arcade.Sprite("platform.png",.3)
            plat.center_x = coord[0]
            plat.center_y = coord[1]
            self.block_list.append(plat)  
        plat_vert_coords = [(180,490),(220,110),(220,210),(220,310),(520,490)]        
        for coord in plat_vert_coords:
            plat_vert = arcade.Sprite("platform_vert.png",.3)
            plat_vert.center_x = coord[0]
            plat_vert.center_y = coord[1]
            self.block_list.append(plat_vert)    
        plat_vert_long_coords = [(320,350),(620,250),(1200,300)]        
        for coord in plat_vert_long_coords:
            plat_vert_long = arcade.Sprite("platform_long.png",.3)
            plat_vert_long.angle = 90
            plat_vert_long.center_x = coord[0]
            plat_vert_long.center_y = coord[1]
            self.block_list.append(plat_vert_long)
        
    def setup(self):
        "make start screen and restart variables"
        
        """Player Setup"""
        self.player.center_x = 100
        self.player.center_y = 100        
        self.player.changeX = 0
        self.player.changeY = 0
        self.W_pressed = False
        self.A_pressed = False
        self.S_pressed = False
        self.D_pressed = False
        self.R_pressed = False 
        self.SPACE_pressed = False
        self.can_shift = True
        self.health = 3
        self.immune = False
        self.score = 0

        
        """Global Setup"""
        self.start = True
        self.speed = 5
        self.gravity_constant = 10
        self.player.change_y = -self.gravity_constant
        self.up = True
        self.distance = self.player.center_x
        self.immune_start = 0
                
        self.ring_list.update_animation()
        
        
        
        
        """Obstacle Setup"""
        self.scroll = 0
                
                
        """SFX and Music Setup"""  
        '''
        playlist = []
        randSelect = random.randint(0,(len(playlist)-1))
        self.selection = playlist[randSelect]        
        if self.sfx:
            os.system(self.selection)
            
        if not(self.sfx):
            winsound.PlaySound(self.selection, winsound.SND_ASYNC)
        '''   
        """Menu Setup"""

 
    def menu(self):
        "run start screen"
            
    def on_draw(self):
        arcade.start_render()        
        
        if self.start:
            "draw game elements"
            self.background.center_x += self.scroll/5
            self.background.draw()
            
            for sprite in self.block_list:
                sprite.center_x += self.scroll
            for sprite in self.spike_list:
                sprite.center_x += self.scroll
            for sprite in self.ring_list:
                sprite.center_x += self.scroll   
            
            self.scroll = 0
            
            self.spike_list.draw()
            self.block_list.draw()
            self.player.draw()
            self.ring_list.draw()
            
            
            self.player.update_animation()
            self.ring_list.update_animation()
            
            
            
            
            arcade.draw_text(f"Health:{self.health: 2.0f}",25, SCREEN_HEIGHT +15,arcade.color.BLACK,15)
            arcade.draw_rectangle_filled(120 + self.health * 10 , SCREEN_HEIGHT +20, self.health*20, 20, arcade.color.RED)
            arcade.draw_rectangle_outline(150, SCREEN_HEIGHT +20, 60, 20, arcade.color.BLACK)
    
            
        else:
            "draw menu"

    def update(self,dt):
        "move stuff"
    
        if self.start:
            "Do whle game runs"
            print(self.distance)
            print(len(self.spike_list))
    
            if self.player.center_x < 100 and self.distance > 110:
                self.scroll = 5
                self.player.center_x += self.scroll    
            if self.player.center_x > 4*SCREEN_WIDTH/5 and self.distance < 2430:
                self.scroll = -5
                self.player.center_x += self.scroll
            
            
            self.player.change_x = 0
                                  
            if self.A_pressed and self.can_shift:
                self.player.change_x = -self.speed

            if self.D_pressed and self.can_shift:
                self.player.change_x = self.speed
                
            
            self.player.center_x += self.player.change_x 
            self.distance += self.player.change_x
            block_hit_list = arcade.check_for_collision_with_list(self.player,self.block_list)
            if len(block_hit_list) != 0:
                self.player.center_x -= self.player.change_x
                self.distance -= self.player.change_x 
                
            
            self.player.center_y += self.player.change_y 
            block_hit_list = arcade.check_for_collision_with_list(self.player,self.block_list)
            if len(block_hit_list) != 0:
                for block in block_hit_list:
                    if block.center_y > self.player.center_y and not(self.up):
                        self.can_shift = True
                    elif block.center_y < self.player.center_y and self.up: 
                        self.can_shift = True
                    else:
                        self.can_shift = False
                        
                self.player.center_y -= self.player.change_y
                
            else:
                self.can_shift = False
                
            block_hit_list = arcade.check_for_collision_with_list(self.player,self.block_list)
            if len(block_hit_list) != 0:
                for block in block_hit_list:
                    if block.center_x > self.player.center_x:
                        self.player.center_x -= 1
                    else: 
                        self.player.center_x += 1
                        
            spike_hit_list = arcade.check_for_collision_with_list(self.player,self.spike_list)
            if len(spike_hit_list) != 0 and self.immune == False:
                self.health -= 1
                self.immune = True
                self.immune_start = time.time()
            
            if time.time() - self.immune_start >= 2:
                self.immune = False
                
                
            ring_hit_list = arcade.check_for_collision_with_list(self.player,self.ring_list)
            if len(ring_hit_list) != 0: 
                for ring in ring_hit_list:
                    ring.kill()
                    self.score += 1

                
                
        else:
            self.menu()
            
            
    def on_mouse_motion(self,x,y,dx,dy):
        
        self.mousePos_x = x
        self.mousePos_y = y
        
        if self.start:
            "while game runs"
            
        else:
            "menu screen"
          
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        self.mouseClick_x = x
        self.mouseClick_y = y
        
            
    def on_key_press(self,key,modifiers):
 
        if key == arcade.key.W:
            self.W_pressed = True
        if key == arcade.key.A:
            self.A_pressed = True
        if key == arcade.key.S:
            self.S_pressed = True
        if key == arcade.key.D:
            self.D_pressed = True
        if key == arcade.key.SPACE:
            self.SPACE_pressed = True
            if self.can_shift:
                self.player.change_y = -self.player.change_y
                self.up = not(self.up)
                self.can_shift = False
            
    def on_key_release(self,key,modifiers):
        
        if key == arcade.key.W:
            self.W_pressed = False
        if key == arcade.key.A:
            self.A_pressed = False
        if key == arcade.key.S:
            self.S_pressed = False
        if key == arcade.key.D:
            self.D_pressed = False
        if key == arcade.key.SPACE:
            self.SPACE_pressed = False
        
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT+40, "Drawing Example")
    window.setup()
    arcade.run()
        
main()