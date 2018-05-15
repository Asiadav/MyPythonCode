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
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()
        self.crate_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        self.enemy_raycast = arcade.SpriteList()
        
        for i in range(2):
            background = arcade.Sprite("background.jpg")
            background.center_y = i * SCREEN_HEIGHT/3 
            self.background_list.append(background)
        for i in range(2):
            background = arcade.Sprite("background.jpg")
            background.center_y = i * SCREEN_HEIGHT/3 
            background.center_x = i * SCREEN_WIDTH/3
            self.background_list.append(background)
        
        self.player = arcade.Sprite("player.png",0.2)
        self.crosshair = arcade.Sprite("crosshair.png",0.1)   
        self.enemy = arcade.Sprite("player.png", 0.2)
        
        self.rip = arcade.Sprite("RIP.png", 0.2)
        self.win = arcade.Sprite("medal.png", 0.5)
        
        self.enemy_list.append(self.enemy)
        self.player_list.append(self.player)
        
        self.gameExplain = arcade.Sprite("gameExplain.png",.5)
        self.gameExplain.center_x = SCREEN_WIDTH//2 + 100
        self.gameExplain.center_y = 160
        
        self.controls = arcade.Sprite("controls.png",.3)
        self.controls.center_x = 275
        self.controls.center_y = SCREEN_HEIGHT - 125        
        """End"""
        
    def setup(self):
        "make start screen and restart variables"
        
        """Player Setup"""
        self.player.center_x = 20
        self.player.center_y = 20        
        self.health = 10
        self.player.prevAngle = 0
        self.player.changeX = 0
        self.player.changeY = 0        
        self.reloading = False
        self.reload_counter = 0
        self.W_pressed = False
        self.A_pressed = False
        self.S_pressed = False
        self.D_pressed = False
        self.R_pressed = False    
        self.canMoveLeft = True
        self.canMoveRight = True
        self.canMoveDown = True
        self.canMoveUp = True     
        self.left_down = False
        self.clip = 10
        self.clip_full = self.clip
        """End"""
        
        
        """Enemy Setup"""
        self.shot_time = 0
        self.enemy_shoot_time = 0
        self.enemy.center_x = SCREEN_WIDTH - 30
        self.enemy.center_y = SCREEN_HEIGHT - 30
        self.enemy.prevX = 0
        self.enemy.prevY = 0          
        self.stuck_count = 0
        self.enemy_health = 20    
        self.shooting = False
        self.raycast_time = 0
        self.turn_time = 0
        """End"""

        
        """Global Setup"""
        self.speed = 3
        self.bullet_speed = 18      
        self.won = False
        self.lost = False
        self.start = False
        self.bullet_spread = 5
        self.sfx = False 
        self.menuPos = 1
        """End"""
        
        
        """Obstacle Setup"""
        counter = 0
        placing_sprites = True
        
        while placing_sprites:
            counter += 2
            rock = arcade.Sprite("rock.png", .8)
            rock.center_x = random.randrange(60,SCREEN_WIDTH-60)
            rock.center_y = random.randrange(60,SCREEN_HEIGHT-60)
            self.rock_list.append(rock)
            
            for item in self.rock_list:
                exception = self.rock_list.pop()
                no_no_list = arcade.check_for_collision_with_list(item,self.rock_list)
                for no_no in no_no_list:
                    no_no.kill()
                    counter -=1
                self.rock_list.append(exception)

       
            crate = arcade.Sprite("crate.png", .1)
            crate.center_x = random.randrange(60,SCREEN_WIDTH-60)
            crate.center_y = random.randrange(60,SCREEN_HEIGHT-60)
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
                no_no_list = arcade.check_for_collision_with_list(item,self.rock_list)
                for no_no in no_no_list:
                    no_no.kill()
                    counter -=1
                self.crate_list.append(exception)
                
            no_no_list = arcade.check_for_collision_with_list(self.player,self.rock_list)
            for no_no in no_no_list:
                no_no.kill()
                counter -= 1
                
            no_no_list = arcade.check_for_collision_with_list(self.player,self.crate_list)
            for no_no in no_no_list:
                no_no.kill()
                counter -= 1
            
            if counter >= 25:
                placing_sprites = False
        """End"""        
                
        """SFX and Music Setup"""        
        if self.sfx:
            os.system("danger.mp3")
            
        if not(self.sfx):
            playlist = ["danger.wav","waveshaper.wav","danger2.wav","danger3.5.wav","hangem.wav","mine.wav","onlychance.wav","wisdomrage.wav"]
            selection = playlist[random.randint(0,len(playlist)-1)]
            winsound.PlaySound(selection, winsound.SND_ASYNC)
        """End"""
            
        """Menu Setup"""
        self.onButton = 1
        self.color1 = arcade.color.WHITE
        self.color2 = arcade.color.BLACK        
        """End"""
 
    def menu(self):
        "run start screen"
        if self.menuPos == 1:
            "Start Game"
            
        if self.menuPos == 2:
            "Toggle SFX"
            
    def on_draw(self):
        
        arcade.start_render()        
        
        if self.start:
            self.background_list.draw()
            
            self.enemy_raycast.draw()
            self.player_list.draw()
            self.enemy_list.draw()
            self.bullet_list.draw()
            self.rock_list.draw()
            self.crate_list.draw()
            self.enemy_bullet_list.draw()
            self.crosshair.draw()
            
            if 0 < self.enemy_health < 20:
                arcade.draw_rectangle_filled(self.enemy.center_x + (self.enemy_health -20 ), self.enemy.center_y +20, 2 * self.enemy_health , 10, arcade.color.GREEN)        
            
            arcade.draw_triangle_filled(self.player.center_x, self.player.center_y + 30,self.player.center_x - 10, self.player.center_y + 40,self.player.center_x + 10, self.player.center_y + 40,arcade.color.RED)
            arcade.draw_rectangle_filled(SCREEN_WIDTH//2,SCREEN_HEIGHT+20,SCREEN_WIDTH,40,arcade.color.WHITE)
            
            arcade.draw_text(f"Health:{self.health: 2.0f}",25, SCREEN_HEIGHT +15,arcade.color.BLACK,15)
            arcade.draw_rectangle_filled(120 + self.health * 4 , SCREEN_HEIGHT +20, self.health*8, 20, arcade.color.RED)
            arcade.draw_rectangle_outline(160, SCREEN_HEIGHT +20, 80, 20, arcade.color.BLACK)
            
            arcade.draw_text(f"Clip:{self.clip: 2.0f}",250, SCREEN_HEIGHT +15,arcade.color.BLACK,15)        
        
            if self.reloading:      
                arcade.draw_text("Reloading",SCREEN_WIDTH//2 + 200, SCREEN_HEIGHT +15,arcade.color.BLACK,15)
                arcade.draw_rectangle_filled(self.crosshair.center_x + 20, self.crosshair.center_y, 10, 40, arcade.color.WHITE)
                arcade.draw_rectangle_filled(self.crosshair.center_x + 20, self.crosshair.center_y + self.reload_counter / 4 - 20, 10, self.reload_counter/2, arcade.color.BLACK)
            
            if self.health <= 0:
                arcade.draw_rectangle_filled(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT + 80, arcade.color.BLACK)
                arcade.draw_text("You Lost",SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT//2 + 30,arcade.color.WHITE,20)
                self.rip.center_x = SCREEN_WIDTH//2
                self.rip.center_y = SCREEN_HEIGHT//2 - 20
                self.rip.draw()
                if self.lost == False and self.won == False:
                    winsound.PlaySound("lose.wav", winsound.SND_ASYNC)
                self.lost = True
                
            if self.enemy_health <= 0:
                arcade.draw_rectangle_filled(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT + 80, arcade.color.BLACK)
                arcade.draw_text("You Win",SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT//2 + 30,arcade.color.WHITE,20) 
                self.win.center_x = SCREEN_WIDTH//2 - 30
                self.win.center_y = SCREEN_HEIGHT//2 - 40
                self.win.draw()            
                if self.won == False and self.lost == False:
                    winsound.PlaySound("win1.wav", winsound.SND_ASYNC)
                self.won = True        
        else:
            
            arcade.draw_rectangle_filled(SCREEN_WIDTH//2 + 220, SCREEN_HEIGHT//2 + 220, 300, 40, self.color1)
            arcade.draw_text("Start Game",SCREEN_WIDTH//2 + 160, SCREEN_HEIGHT//2 + 210,self.color2,20)
            
            arcade.draw_rectangle_filled(SCREEN_WIDTH//2 + 220, SCREEN_HEIGHT//2 + 180, 300, 40, self.color2)
            arcade.draw_text("SFX",SCREEN_WIDTH//2 + 170, SCREEN_HEIGHT//2 + 170,self.color1,20)
            
            if self.sfx:
                arcade.draw_text("On",SCREEN_WIDTH//2 + 220, SCREEN_HEIGHT//2 + 170,self.color1,20)
            else:
                arcade.draw_text("Off",SCREEN_WIDTH//2 + 220, SCREEN_HEIGHT//2 + 170,self.color1,20)
                arcade.draw_text("(recommended)",SCREEN_WIDTH//2 + 160, SCREEN_HEIGHT//2 + 140,arcade.color.WHITE,12)
            
            self.gameExplain.draw()
            self.controls.draw()
            
            if self.menuPos == 1:
                "Start Game"
            if self.menuPos == 2:
                "Toggle SFX"

    def enemy_action(self):
        "what the enemy does" 
        
        self.enemy.angle = math.degrees(math.atan2((self.enemy.center_y - self.player.center_y),(self.enemy.center_x - self.player.center_x))) - 180
        
        if time.time()-self.turn_time> 1:
            "run once per time"
            self.turn_time = time.time()
            self.enemy.changeX =  math.cos(math.radians(self.enemy.angle + random.randint(-75,75))) * 2
            self.enemy.changeY = math.sin(math.radians(self.enemy.angle + random.randint(-75,75))) * 2

        self.enemy.center_x += self.enemy.changeX 
        crate_hit_list = arcade.check_for_collision_with_list(self.enemy,self.crate_list)
        rock_hit_list = arcade.check_for_collision_with_list(self.enemy,self.rock_list)
        player_hit_list = arcade.check_for_collision_with_list(self.enemy,self.player_list)
        if len(crate_hit_list) != 0 or len(rock_hit_list) != 0 or len(player_hit_list) != 0:
            self.enemy.center_x -= self.enemy.changeX 
        
        self.enemy.center_y += self.enemy.changeY
        crate_hit_list = arcade.check_for_collision_with_list(self.enemy,self.crate_list)
        rock_hit_list = arcade.check_for_collision_with_list(self.enemy,self.rock_list)
        player_hit_list = arcade.check_for_collision_with_list(self.enemy,self.player_list)
        if len(crate_hit_list) != 0 or len(rock_hit_list) != 0 or len(player_hit_list) != 0:
            self.enemy.center_y -= self.enemy.changeY       
            
        if self.enemy.center_x == self.enemy.prevX and self.enemy.center_y == self.enemy.prevY:
            self.stuck_count += 1
        
        if time.time() - self.raycast_time > 1/8:
            self.raycast_time = time.time()
            raycast = arcade.Sprite("bullet.png",.05)  
            raycast.alpha = 0
            raycast.center_x = self.enemy.center_x - math.cos(math.radians(self.enemy.angle + 90)) * 12
            raycast.center_y = self.enemy.center_y - math.sin(math.radians(self.enemy.angle + 90)) * 12
    
            raycast.angle = self.enemy.angle - 90 
    
            self.enemy_raycast.append(raycast)               
        
        if self.shooting and time.time() - self.enemy_shoot_time > 1/4:
            self.enemy_shoot_time = time.time()
            
            bullet = arcade.Sprite("bullet.png",.05)
                
            if self.sfx:
                winsound.PlaySound("shot1.wav", winsound.SND_ASYNC)
                
            bullet.center_x = self.enemy.center_x - math.cos(math.radians(self.enemy.angle + 90)) * 12 
            bullet.center_y = self.enemy.center_y - math.sin(math.radians(self.enemy.angle + 90)) * 12
    
            bullet.angle = math.degrees(math.atan2((bullet.center_y - self.player.center_y),(bullet.center_x - self.player.center_x))) + 90 + random.randrange(-self.bullet_spread,self.bullet_spread)
              
            self.enemy_bullet_list.append(bullet)            
            self.shooting = False
            
        if self.stuck_count >= 3:
            self.stuck_count = 0
            self.enemy.center_x -= self.enemy.changeX
            self.enemy.center_y -= self.enemy.changeY
        
        if self.enemy.center_x < 15 or self.enemy.center_x > SCREEN_WIDTH-15:
            self.enemy.center_x -= self.enemy.changeX
        if self.enemy.center_y < 15 or self.enemy.center_y > SCREEN_HEIGHT-25:
            self.enemy.center_y -= self.enemy.changeY
            
        if self.enemy.center_x < 15:
            self.enemy.center_x += self.speed
        if self.enemy.center_y < 15:
            self.enemy.center_y += self.speed
        if self.enemy.center_x > SCREEN_WIDTH - 15:
            self.enemy.center_x -= self.speed
        if self.enemy.center_y > SCREEN_HEIGHT - 15:
            self.enemy.center_y -= self.speed
        
        self.enemy.prevX = self.enemy.center_x
        self.enemy.prevY = self.enemy.center_y
        
    def update(self,dt):
        "move stuff"
    
        if self.start:
        
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
            
            if (self.R_pressed and self.clip < self.clip_full) or self.reloading:
                if self.sfx and self.reloading == False:
                    winsound.PlaySound("reload2.wav", winsound.SND_ASYNC)
                self.reloading = True
                self.reload_counter += 1
                if self.reload_counter >= 80:
                    self.reloading = False
                    self.clip = self.clip_full
                    self.reload_counter = 0
              
            for bullet in self.bullet_list:
                bullet.center_x += math.cos(math.radians(bullet.angle + 90)) * self.bullet_speed
                bullet.center_y += math.sin(math.radians(bullet.angle + 90)) * self.bullet_speed
                rock_hit_list = arcade.check_for_collision_with_list(bullet,self.rock_list)
                crate_hit_list = arcade.check_for_collision_with_list(bullet,self.crate_list)
                enemy_hit_list = arcade.check_for_collision_with_list(bullet,self.enemy_list)
                if len(rock_hit_list) > 0:
                    bullet.kill()
                if len(crate_hit_list) > 0:
                    bullet.kill()
                if len(enemy_hit_list) > 0:
                    self.enemy_health -= 1
                    bullet.kill()
                    
                if -20 > bullet.center_x > SCREEN_WIDTH + 20 and -20 > bullet.center_y > SCREEN_HEIGHT + 20:
                    bullet.kill()
                    
            for bullet in self.enemy_bullet_list:
                bullet.center_x += math.cos(math.radians(bullet.angle + 90)) * self.bullet_speed
                bullet.center_y += math.sin(math.radians(bullet.angle + 90)) * self.bullet_speed 
                rock_hit_list = arcade.check_for_collision_with_list(bullet,self.rock_list)
                crate_hit_list = arcade.check_for_collision_with_list(bullet,self.crate_list)
                player_hit_list = arcade.check_for_collision_with_list(bullet,self.player_list)
                if len(rock_hit_list) > 0:
                    bullet.kill()
                if len(crate_hit_list) > 0:
                    bullet.kill()
                if len(player_hit_list) > 0:
                    self.health -= 1
                    bullet.kill()
                    
                if -20 > bullet.center_x > SCREEN_WIDTH + 20 and -20 > bullet.center_y > SCREEN_HEIGHT + 20:
                    bullet.kill()
                    
            for bullet in self.enemy_raycast:
                bullet.center_x += math.cos(math.radians(bullet.angle + 90)) * self.bullet_speed *2.5
                bullet.center_y += math.sin(math.radians(bullet.angle + 90)) * self.bullet_speed *2.5
                rock_hit_list = arcade.check_for_collision_with_list(bullet,self.rock_list)
                crate_hit_list = arcade.check_for_collision_with_list(bullet,self.crate_list)
                player_hit_list = arcade.check_for_collision_with_list(bullet,self.player_list)
                if len(rock_hit_list) > 0:
                    bullet.kill()
                if len(crate_hit_list) > 0:
                    bullet.kill()
                if len(player_hit_list) > 0:
                    self.shooting = True
                    bullet.kill()
                    
                if -20 > bullet.center_x > SCREEN_WIDTH + 20 and -20 > bullet.center_y > SCREEN_HEIGHT + 20:
                    bullet.kill()
                    
            self.player.center_x += self.player.changeX 
            crate_hit_list = arcade.check_for_collision_with_list(self.player,self.crate_list)
            rock_hit_list = arcade.check_for_collision_with_list(self.player,self.rock_list)
            enemy_hit_list = arcade.check_for_collision_with_list(self.enemy,self.enemy_list)        
            if len(crate_hit_list) != 0 or len(rock_hit_list) != 0 or len(enemy_hit_list) != 0:
                self.player.center_x -= self.player.changeX 
            
            self.player.center_y += self.player.changeY
            crate_hit_list = arcade.check_for_collision_with_list(self.player,self.crate_list)
            rock_hit_list = arcade.check_for_collision_with_list(self.player,self.rock_list)
            enemy_hit_list = arcade.check_for_collision_with_list(self.enemy,self.enemy_list)                
            if len(crate_hit_list) != 0 or len(rock_hit_list) != 0 or len(enemy_hit_list) != 0:
                self.player.center_y -= self.player.changeY       
        
            if self.player.center_x < 15 or self.player.center_x > SCREEN_WIDTH-15:
                self.player.center_x -= self.player.changeX
            if self.player.center_y < 15 or self.player.center_y > SCREEN_HEIGHT-25:
                self.player.center_y -= self.player.changeY
        
            self.enemy_action()        
        else:
            self.menu()
    def on_mouse_motion(self,x,y,dx,dy):
        
        self.mousePos_x = x
        self.mousePos_y = y
        
        self.onButton = 0       
        
        if SCREEN_WIDTH//2 + 40 < self.mousePos_x < SCREEN_WIDTH//2 + 400 and   SCREEN_HEIGHT//2 + 200 < self.mousePos_y < SCREEN_HEIGHT//2 + 240:
            self.onButton = 1
            self.color1 = arcade.color.WHITE
            self.color2 = arcade.color.BLACK
        if SCREEN_WIDTH//2 + 40 < self.mousePos_x < SCREEN_WIDTH//2 + 400 and   SCREEN_HEIGHT//2 + 160 < self.mousePos_y < SCREEN_HEIGHT//2 + 200:
            self.onButton = 2
            self.color1 = arcade.color.BLACK
            self.color2 = arcade.color.WHITE   
            
        if self.start:
            self.crosshair.center_x = self.mousePos_x 
            self.crosshair.center_y = self.mousePos_y
        
            self.player.angle = math.degrees(math.atan2((self.player.center_y - self.crosshair.center_y),(self.player.center_x - self.crosshair.center_x))) -180
        
            crate_hit_list = arcade.check_for_collision_with_list(self.player,self.crate_list)
            rock_hit_list = arcade.check_for_collision_with_list(self.player,self.rock_list)
            if len(crate_hit_list) != 0 or len(rock_hit_list) != 0:
                if -360<self.player.angle<-315 or -45<self.player.angle<0:
                    self.player.center_x -= self.speed
        
                    crate_hit_list = arcade.check_for_collision_with_list(self.player,self.crate_list)
                    rock_hit_list = arcade.check_for_collision_with_list(self.player,self.rock_list)
                    if len(crate_hit_list) != 0 or len(rock_hit_list) != 0:
                        self.player.center_x += self.speed     
        
                if -315<self.player.angle<-225:
                    self.player.center_y -= self.speed
        
                    crate_hit_list = arcade.check_for_collision_with_list(self.player,self.crate_list)
                    rock_hit_list = arcade.check_for_collision_with_list(self.player,self.rock_list)
                    if len(crate_hit_list) != 0 or len(rock_hit_list) != 0:
                        self.player.center_y += self.speed        
        
                if -225<self.player.angle<-135:
                    self.player.center_x += self.speed
        
                    crate_hit_list = arcade.check_for_collision_with_list(self.player,self.crate_list)
                    rock_hit_list = arcade.check_for_collision_with_list(self.player,self.rock_list)
                    if len(crate_hit_list) != 0 or len(rock_hit_list) != 0:
                        self.player.center_x -= self.speed        
        
                if -135<self.player.angle<-45:
                    self.player.center_y += self.speed
        
                    crate_hit_list = arcade.check_for_collision_with_list(self.player,self.crate_list)
                    rock_hit_list = arcade.check_for_collision_with_list(self.player,self.rock_list)
                    if len(crate_hit_list) != 0 or len(rock_hit_list) != 0:
                        self.player.center_y -= self.speed        
        
                self.player.angle = self.player.prevAngle   
        
            else:
                self.player.angle = math.degrees(math.atan2((self.player.center_y - self.crosshair.center_y),(self.player.center_x - self.crosshair.center_x))) -180
                self.player.prevAngle = self.player.angle        
            
          
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        self.mouseClick_x = x
        self.mouseClick_y = y
        
        if self.onButton == 1 and button == arcade.MOUSE_BUTTON_LEFT and self.start == False:
            self.set_mouse_visible(False)
            self.start = 1        
            if self.sfx:
                playlist = ["danger.wav","waveshaper.wav","danger2.wav","danger3.5.wav","hangem.wav","mine.wav","onlychance.wav","wisdomrage.wav"]
                selection = playlist[random.randint(0,len(playlist)-1)]                
                os.system(selection)
        if self.onButton == 2 and button == arcade.MOUSE_BUTTON_LEFT and self.start == False:
            if self.sfx:
                self.sfx = False
            else:
                self.sfx = True
            
        if button == arcade.MOUSE_BUTTON_LEFT and self.clip > 0 and time.time() - self.shot_time > 1/4 and self.start:
            self.shot_time = time.time()
            
            self.clip -= 1
            bullet = arcade.Sprite("bullet.png",.05)
            
            if self.sfx:
                
                playlist = ["shot1.wav","shot2.wav","shot3.wav","shot4.wav"]
                selection = playlist[random.randint(0,len(playlist)-1)]                
                winsound.PlaySound(selection, winsound.SND_ASYNC)
            
            bullet.center_x = self.player.center_x - math.cos(math.radians(self.player.angle + 90)) * 12
            bullet.center_y = self.player.center_y - math.sin(math.radians(self.player.angle + 90)) * 12

            bullet.angle = math.degrees(math.atan2((bullet.center_y - self.crosshair.center_y),(bullet.center_x - self.crosshair.center_x))) + 90 + random.randrange(-self.bullet_spread,self.bullet_spread) 
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