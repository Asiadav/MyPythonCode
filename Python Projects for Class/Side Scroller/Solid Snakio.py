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

class Enemy(arcade.AnimatedTimeSprite):
    def __init__(self, x, y):
        super().__init__(self)
        self.center_x = x
        self.center_y = y
        self.scale = 0.15     
        self.textures = []
        self.textures.append(arcade.load_texture("goomba.png"))
        self.textures.append(arcade.load_texture("goomba.png", mirrored = True)) 
        
class EnemyFlat(arcade.AnimatedTimeSprite):
    def __init__(self, x, y):
        super().__init__(self)
        self.center_x = x
        self.center_y = y
        self.scale = 0.15     
        self.textures = []
        self.textures.append(arcade.load_texture("goomba_flat1.png"))         
        self.textures.append(arcade.load_texture("goomba_flat2.png"))         
        self.textures.append(arcade.load_texture("goomba_flat3.png"))         
        self.textures.append(arcade.load_texture("goomba_flat4.png"))         
        
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
        self.menu_sprite_list = arcade.SpriteList()
        
        self.menu_button1 = arcade.Sprite("BR.png",0.2)
        self.menu_button1.alpha = 0.5
        self.menu_button1.center_x = SCREEN_WIDTH//2
        self.menu_button1.center_y = SCREEN_HEIGHT//2 + 150
        self.menu_sprite_list.append(self.menu_button1)        
        
        self.menu_button2 = arcade.Sprite("BR.png",0.2)
        self.menu_button2.alpha = 0.5        
        self.menu_button2.center_x = SCREEN_WIDTH//2
        self.menu_button2.center_y = SCREEN_HEIGHT//2 +75
        self.menu_sprite_list.append(self.menu_button2)  
        
        self.menu_button3 = arcade.Sprite("BR.png",0.2)
        self.menu_button3.alpha = 0.5        
        self.menu_button3.center_x = SCREEN_WIDTH//2
        self.menu_button3.center_y = SCREEN_HEIGHT//2 
        self.menu_sprite_list.append(self.menu_button3)          
        
        self.cursor = arcade.Sprite("goomba.png",0.05)
        self.cursor.alpha = 0
        
        self.menu = arcade.Sprite("menu.png",0.7)
        self.menu.center_x = SCREEN_WIDTH//2 + 10
        self.menu.center_y = SCREEN_HEIGHT//2 + 20
        
        self.taco = arcade.Sprite("taco.gif",0.25)   
        self.taco.center_x = 2485
        self.taco.center_y = 80        
        self.rip = arcade.Sprite("RIP.png", 0.2)
        self.win = arcade.Sprite("medal.png", 0.5)
        
        self.background = arcade.Sprite("background.png",1.95)
        self.background.center_x = SCREEN_WIDTH 
        self.background.center_y = SCREEN_HEIGHT//2
        
        self.player_list = arcade.SpriteList()
        self.player = Player(SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
        self.player.update_animation()
        
        self.block_list = arcade.SpriteList() 
        self.ring_list = arcade.SpriteList()
        self.spike_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        
        
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
        
        #note to self: never use coordinate based sprite placing for large numbers of sprites. It is too tedious
        
        enemy_coords = [(60,300),(580,60),(375,200),(555,300),(700,60),(800,60),(900,60),(1000,400),(1420,290),(1450,60),(1800,60),(1900,60),(1800,510)]        
        for coord in enemy_coords:
            enemy = Enemy(coord[0],coord[1])         
            enemy.change_y = -4
            enemy.change_x = random.uniform(1,3)
            self.enemy_list.append(enemy)        
        ring_coords = [(60,200),(65,535),(220,535),(250,535),(280,535),(400,390),(585,290),(850,60),(880,60),(910,60),(950,400),(1330,290),(1440,60),(1700,200),(1870,60),(1810,60),(1965,510)]        
        for coord in ring_coords:
            ring = Ring(coord[0],coord[1])           
            self.ring_list.append(ring)
        spike_coords = [(100,170,180),(450,250,90),(360,550,180),(1120,550,180),(1425,450,0),(1480,60,0),(1780,300,270),(1790,230,0),(1840,50,0),(1730,470,90),(1840,555,180),(1965,440,180)]        
        for coord in spike_coords:
            spikes = arcade.Sprite("spikes.png",.25)
            spikes.angle = coord[2]
            spikes.center_x = coord[0]
            spikes.center_y = coord[1]
            self.spike_list.append(spikes)        
        block_coords = [(60,240),(60,470),(100,200),(130,200),(400,350),(480,285),(850,305),(1080,305),(1285,60),(1370,285),(1520,60),(1760,505),(2000,505)]        
        for coord in block_coords:
            block = arcade.Sprite("block.png",.5)
            block.center_x = coord[0]
            block.center_y = coord[1]
            self.block_list.append(block)
        plat_coords = [(170,362),(410,160),(530,250),(705,438),(900,270),(1030,270),(1130,340),(1340,490),(1390,250),(1475,420),(1525,250),(1700,300),(1810,470),(1840,200),(1950,470)]        
        for coord in plat_coords:
            plat = arcade.Sprite("platform.png",.3)
            plat.center_x = coord[0]
            plat.center_y = coord[1]
            self.block_list.append(plat)  
        plat_vert_coords = [(180,490),(220,110),(220,210),(220,310),(520,490),(950,490),(1100,110),(1700,110)]        
        for coord in plat_vert_coords:
            plat_vert = arcade.Sprite("platform_vert.png",.3)
            plat_vert.center_x = coord[0]
            plat_vert.center_y = coord[1]
            self.block_list.append(plat_vert)    
        plat_vert_long_coords = [(320,350),(620,250),(1210,300),(1610,350),(2000,250)]        
        for coord in plat_vert_long_coords:
            plat_vert_long = arcade.Sprite("platform_long.png",.3)
            plat_vert_long.angle = 90
            plat_vert_long.center_x = coord[0]
            plat_vert_long.center_y = coord[1]
            self.block_list.append(plat_vert_long)
        
    def setup(self):
        "make start screen and restart variables"
        
        """Player Setup"""
        self.player.center_x = 60
        self.player.center_y = 60        
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
        self.objective = False
        self.lost = False
        self.won = False
        self.sfx = False
        self.start = False
        self.speed = 4
        self.gravity_constant = 10
        self.player.change_y = -self.gravity_constant
        self.up = True
        self.distance = self.player.center_x
        self.immune_start = 0
        self.music = True
        self.ring_list.update_animation()
        self.player.update_animation()
        self.enemy_list.update_animation()
        self.toggle = True
        self.scrolling = False
        self.enemy_killed = False
        
        self.enemy_kill_start = 0
        """Obstacle Setup"""
        self.scroll = 0
                   
        """SFX and Music Setup"""  
        
        playlist = ['Africa.wav','Blue.wav','Centuries.wav','Feeling.wav','September.wav','Stop.wav','Take.wav','Under.wav','Warriors.wav','Wayward.wav','Wicked.wav']
        randSelect = random.randint(0,(len(playlist)-1))
        self.selection = playlist[randSelect]        
    
        winsound.PlaySound("Skyrim.wav", winsound.SND_ASYNC)
        

    def on_draw(self):
        arcade.start_render()        
        
        if self.start:
            "draw game elements"
            self.background.center_x += self.scroll/5
            self.taco.center_x += self.scroll
            self.background.draw()
            
            if self.scrolling:
                self.player.center_x += self.scroll
                self.scrolling = False
            
            for sprite in self.block_list:
                sprite.center_x += self.scroll
            for sprite in self.spike_list:
                sprite.center_x += self.scroll
            for sprite in self.ring_list:
                sprite.center_x += self.scroll   
            for sprite in self.enemy_list:
                sprite.center_x += self.scroll
                
            if self.immune and round(time.time() - self.immune_start,1) % 0.5 == 0:
                self.player.alpha = 0.2
            elif self.immune:
                self.player.alpha = 0.8
                
            if self.immune == False:
                self.player.alpha = 1.0
            
            self.scroll = 0
            self.taco.draw()
            self.enemy_list.draw()
            self.spike_list.draw()
            self.block_list.draw()
            self.ring_list.draw()
            
            if self.enemy_killed:
                self.kill_animation.draw()
                self.kill_animation.update_animation()                    
            
            self.player.draw()
                
            self.player.update_animation()
            self.ring_list.update_animation()
            self.enemy_list.update_animation()
            
            if self.health <= 0 and self.won == False:
                arcade.draw_rectangle_filled(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT + 80, arcade.color.BLACK)
                arcade.draw_text("You Lost",SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT//2 + 30,arcade.color.WHITE,20)
                self.rip.center_x = SCREEN_WIDTH//2
                self.rip.center_y = SCREEN_HEIGHT//2 - 20
                self.rip.draw()
                arcade.draw_text(f"Score:{self.score: 2.0f}",SCREEN_WIDTH//2 - 45, SCREEN_HEIGHT//2 - 100,arcade.color.WHITE,15)
                
                if self.lost == False and self.won == False:
                    winsound.PlaySound("lose.wav", winsound.SND_ASYNC)
                self.lost = True            
            
            else:
                arcade.draw_text(f"Health:{self.health: 2.0f}",25, SCREEN_HEIGHT +15,arcade.color.BLACK,15)
                arcade.draw_rectangle_filled(120 + self.health * 10 , SCREEN_HEIGHT +20, self.health*20, 20, arcade.color.RED)
                arcade.draw_rectangle_outline(150, SCREEN_HEIGHT +20, 60, 20, arcade.color.BLACK)
                
                arcade.draw_text(f"Score:{self.score: 2.0f}",275, SCREEN_HEIGHT +15,arcade.color.BLACK,15)
                            
                
            if self.objective:
                arcade.draw_rectangle_filled(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT + 80, arcade.color.BLACK)
                arcade.draw_text("You Win",SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT//2 + 30,arcade.color.WHITE,20) 
                self.win.center_x = SCREEN_WIDTH//2 - 30
                self.win.center_y = SCREEN_HEIGHT//2 - 40
                self.win.draw()            
                arcade.draw_text(f"Score:{self.score: 2.0f}",SCREEN_WIDTH//2 - 45, SCREEN_HEIGHT//2 - 100,arcade.color.WHITE,15)
                
                if self.won == False and self.lost == False:
                    self.score = self.health * self.score
                    winsound.PlaySound("win2.wav", winsound.SND_ASYNC)
                self.won = True
        else:
            "draw menu"
            self.menu.draw()
            self.menu_sprite_list.draw()
            
            arcade.draw_text("Start Game",SCREEN_WIDTH//2 - 60, SCREEN_HEIGHT//2 + 140,arcade.color.WHITE,20)         
            arcade.draw_text("Music: ",SCREEN_WIDTH//2 - 60, SCREEN_HEIGHT//2 + 65,arcade.color.WHITE,20)         
            if self.music:
                arcade.draw_text("On",SCREEN_WIDTH//2 + 30, SCREEN_HEIGHT//2 + 65,arcade.color.WHITE,20)         
            else:
                arcade.draw_text("Off",SCREEN_WIDTH//2 + 30, SCREEN_HEIGHT//2 + 65,arcade.color.WHITE,20)         
                winsound.PlaySound("win2.wav", winsound.SND_ASYNC)
                
            arcade.draw_text("Useless Toggle: ",SCREEN_WIDTH//2 - 140, SCREEN_HEIGHT//2 - 10,arcade.color.WHITE,20)         
            
            if self.toggle:
                arcade.draw_text("toggled",SCREEN_WIDTH//2 + 40, SCREEN_HEIGHT//2 - 10,arcade.color.WHITE,20)  
            else:
                arcade.draw_text("untoggled",SCREEN_WIDTH//2 + 40, SCREEN_HEIGHT//2 - 10,arcade.color.WHITE,20)         
                
            self.cursor.draw()

                
    def enemy_action(self):
        for enemy in self.enemy_list:
                        
            enemy.center_x += enemy.change_x 
            enemy.center_y += 5
            block_hit_list = arcade.check_for_collision_with_list(enemy,self.block_list)
            if len(block_hit_list) != 0:
                enemy.center_x -= enemy.change_x
                enemy.change_x = -enemy.change_x
            enemy.center_y -= 5
            
            block_hit_list = arcade.check_for_collision_with_list(enemy,self.enemy_list)
            if len(block_hit_list) != 0:    
                enemy.change_x = -enemy.change_x
 
            enemy.center_y += enemy.change_y 
            block_hit_list = arcade.check_for_collision_with_list(enemy,self.block_list)
            if len(block_hit_list) != 0:
                enemy.center_y -= enemy.change_y

    def update(self,dt):
        "move stuff"
    
        if self.start:
            "Do whle game runs"
            self.scroll = False
            
            if self.distance >= 2430:
                self.objective = True
                
            if time.time() - self.enemy_kill_start > 0.3:
                self.enemy_killed = False
            
            if self.player.center_x < 200 and self.distance > 210:
                self.scroll = self.speed
                self.scrolling = True                
                
            if self.player.center_x > 3*SCREEN_WIDTH/5 and self.distance < 2230:
                self.scroll = -self.speed
                self.scrolling = True
            
            
            self.player.change_x = 0
            
            if self.A_pressed and self.can_shift:
                self.player.change_x += -self.speed

            if self.D_pressed and self.can_shift:
                self.player.change_x += self.speed
            
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
                
            enemy_hit_list = arcade.check_for_collision_with_list(self.player,self.enemy_list)
            for enemy in enemy_hit_list:
                kill = False
                if self.player.bottom >= enemy.top - 10 and self.immune == False:
                    self.kill_animation = EnemyFlat(enemy.center_x,enemy.center_y) 
                    self.kill_animation.update_animation()  
                    self.enemy_kill_start = time.time()
                    enemy.kill()
                    self.score += 50
                    self.enemy_killed = True
                    kill = True
            if len(enemy_hit_list) != 0 and self.immune == False and kill == False:
                self.health -= 1
                self.immune = True
                self.immune_start = time.time()
                self.score -= 25
            
            if time.time() - self.immune_start >= 2:
                self.immune = False
                  
                
            ring_hit_list = arcade.check_for_collision_with_list(self.player,self.ring_list)
            if len(ring_hit_list) != 0: 
                for ring in ring_hit_list:
                    ring.kill()
                    self.score += 100
            
            self.enemy_action()
                
        else:
            "do nothing"
            
            
    def on_mouse_motion(self,x,y,dx,dy):
        
        self.mousePos_x = x
        self.mousePos_y = y
        
        if self.start:
            "while game runs"
            
        else:
            "menu screen"
            self.cursor.center_x = x
            self.cursor.center_y = y
            
            self.menu_sprite_list = arcade.SpriteList()

            self.menu_button1 = arcade.Sprite("BR.png",0.2)
            self.menu_button1.alpha = 0.5
            self.menu_button1.center_x = SCREEN_WIDTH//2
            self.menu_button1.center_y = SCREEN_HEIGHT//2 + 150
            self.menu_sprite_list.append(self.menu_button1)        
            
            self.menu_button2 = arcade.Sprite("BR.png",0.2)
            self.menu_button2.alpha = 0.5        
            self.menu_button2.center_x = SCREEN_WIDTH//2
            self.menu_button2.center_y = SCREEN_HEIGHT//2 + 75
            self.menu_sprite_list.append(self.menu_button2)  
            
            self.menu_button3 = arcade.Sprite("BR.png",0.2)
            self.menu_button3.alpha = 0.5        
            self.menu_button3.center_x = SCREEN_WIDTH//2
            self.menu_button3.center_y = SCREEN_HEIGHT//2 
            self.menu_sprite_list.append(self.menu_button3)  
            
            for box in self.menu_sprite_list:
                if arcade.check_for_collision(self.cursor,box):
                    newBox = arcade.Sprite("BR.png",0.25)
                    newBox.alpha = 1
                    newBox.center_x = box.center_x
                    newBox.center_y = box.center_y
                    self.menu_sprite_list.append(newBox)
                    box.kill()
            
            if self.menu_button1 not in self.menu_sprite_list:
                self.button = 1
            elif self.menu_button2 not in self.menu_sprite_list:
                self.button = 2
            elif self.menu_button3 not in self.menu_sprite_list:
                self.button = 3
            else:
                self.button = 0
            
            
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        self.mouseClick_x = x
        self.mouseClick_y = y
        
        if self.start:
            "go nothing"
            
        else:
            
            if self.button == 1:
                self.start = True
                winsound.PlaySound("Here We Go.wav", winsound.SND_ALIAS)
                
                winsound.PlaySound(self.selection, winsound.SND_ASYNC)
                
            if self.button == 2:
                self.music = not(self.music)
                if self.music:
                    winsound.PlaySound("Skyrim.wav", winsound.SND_ASYNC)
                    
            if self.button == 3:
                self.toggle = not(self.toggle)
                self.selection = 'Give.wav'
                
                
    def on_key_press(self,key,modifiers):
 
        if key == arcade.key.W:
            self.W_pressed = True
        if key == arcade.key.A:
            self.A_pressed = True
            if self.up:
                self.player.walk_right_textures = []
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_0.png", mirrored = True))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_1.png", mirrored = True))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_2.png", mirrored = True))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_3.png", mirrored = True))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_5.png", mirrored = True))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_4.png", mirrored = True))     
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_8.png", mirrored = True))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_9.png", mirrored = True))  
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_8.png", mirrored = True)) 
            else:
                self.player.walk_right_textures = []
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_0.png"))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_1.png"))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_2.png"))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_3.png"))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_5.png"))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_4.png"))     
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_8.png"))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_9.png"))  
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_8.png")) 
            
            self.player.update_animation()
                
        if key == arcade.key.S:
            self.S_pressed = True
        if key == arcade.key.D:
            self.D_pressed = True
            if self.up:
                self.player.walk_right_textures = []
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_0.png"))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_1.png"))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_2.png"))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_3.png"))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_5.png"))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_4.png"))     
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_8.png"))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_9.png"))  
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_8.png")) 
            else:
                self.player.walk_right_textures = []
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_0.png", mirrored = True))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_1.png", mirrored = True))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_2.png", mirrored = True))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_3.png", mirrored = True))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_5.png", mirrored = True))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_4.png", mirrored = True))     
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_8.png", mirrored = True))
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_9.png", mirrored = True))  
                self.player.walk_right_textures.append(arcade.load_texture("snake_run_8.png", mirrored = True)) 
                
            self.player.update_animation()
            
        if key == arcade.key.SPACE:
            self.SPACE_pressed = True
            if self.can_shift:
                self.player.change_y = -self.player.change_y
                self.up = not(self.up)
                self.can_shift = False
            
            if self.up:
                self.player.angle = 0
            else:
                self.player.angle = 180
            
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