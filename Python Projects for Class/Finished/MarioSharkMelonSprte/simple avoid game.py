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
        
        
        self.player_list = arcade.SpriteList()
        self.sprite_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.game_list = arcade.SpriteList()
        self.fireball_list = arcade.SpriteList()
        
        self.game_sprite = arcade.Sprite("game.png",.25)
        self.game_list.append(self.game_sprite)
         
        self.score = 0
        self.player_sprite = arcade.Sprite("mario.png",.2)
        
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        
        self.player_list.append(self.player_sprite)
        self.sprites_count = random.randint(30,40)
        
        self.lives = 3
        
        self.immune = True
        self.immuneStart = 0
        
        self.fireball_time = 1.5
        
        
        for i in range(self.sprites_count):
            sprite = arcade.Sprite("sprite.png",.1)
            sprite.center_x = random.randrange(SCREEN_WIDTH)
            sprite.center_y = random.randrange(SCREEN_HEIGHT-40)
            self.sprite_list.append(sprite)        
        
        self.enemy_count = random.randint(20,25)
        for i in range(self.enemy_count):
            sprite = arcade.Sprite("shark.png",.2)
            sprite.center_x = random.randrange(SCREEN_WIDTH)
            sprite.center_y = random.randrange(SCREEN_HEIGHT-20)
            sprite.dx = random.uniform(.5,2)
            self.enemy_list.append(sprite)        
        
        self.start = 0
        self.hit = False
        self.mouse = 0
        self.easy = True
        
        self.fireball_starttime = 0
        self.fireball_time = 1
        self.fireball_count = 3
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(SCREEN_WIDTH/2,SCREEN_HEIGHT+20,SCREEN_WIDTH,40,arcade.color.BLACK)
        
        if self.easy:
            arcade.draw_text("Weak Mode",SCREEN_WIDTH-200,SCREEN_HEIGHT+10,arcade.color.WHITE,20)
        
            
        
        if self.start is 1:
            
            self.fireball_list.draw()
            self.player_list.draw()
            self.sprite_list.draw()
            self.enemy_list.draw()
            
            
            arcade.draw_text(f"Score:{self.score: 2.0f}",10,SCREEN_HEIGHT+10,arcade.color.WHITE,20)
            if self.lives >= 0:
                arcade.draw_text(f"Lives:{self.lives: 2.0f}",120,SCREEN_HEIGHT+10,arcade.color.WHITE,20)
            
            if self.hit:
                arcade.draw_text("You\'ve been hit!",220,SCREEN_HEIGHT+10,arcade.color.WHITE,20)  
            
            if self.score >= self.sprites_count:
                self.hit = False
                arcade.draw_rectangle_filled(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT+100,arcade.color.WHITE)
                arcade.draw_text("GG, WP",SCREEN_WIDTH/2 - 45,SCREEN_HEIGHT/2+10,arcade.color.BLACK,20)
                if self.easy:
                    arcade.draw_text("(But you're still a skrub)",SCREEN_WIDTH/2 - 125,SCREEN_HEIGHT/2-40,arcade.color.BLACK,20)
                    
                
            if self.lives <= 0 and self.score < self.sprites_count:
                self.hit = False
                
                arcade.draw_rectangle_filled(SCREEN_WIDTH/2,SCREEN_HEIGHT+20,SCREEN_WIDTH,40,arcade.color.BLACK)
                
                arcade.draw_text(f"Score:{self.score: 2.0f}",SCREEN_WIDTH/2 - 60,SCREEN_HEIGHT+8,arcade.color.WHITE,30)
                
                arcade.draw_rectangle_filled(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,arcade.color.WHITE)
                arcade.draw_text("Ya Mum Sad",SCREEN_WIDTH/2 - 55,SCREEN_HEIGHT/2,arcade.color.BLACK,20)        
                if self.easy:
                    arcade.draw_text("(Because you lost on easy mode)",SCREEN_WIDTH/2 - 165,SCREEN_HEIGHT/2-40,arcade.color.BLACK,20)                
        
        if self.start < 1:
            arcade.draw_rectangle_filled(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,arcade.color.WHITE)
            arcade.draw_text("Avoid Sharks, Grab Sprites, Shoot Watermelon",SCREEN_WIDTH/2 - 280,SCREEN_HEIGHT/2+140,arcade.color.BLACK,22)  
             
            self.game_sprite.center_x = SCREEN_WIDTH/2
            self.game_sprite.center_y = SCREEN_HEIGHT/2
            self.game_list.draw()
            
            arcade.draw_text("Up arrow to be a real man \n(down arrow to turn easy on)",300,65,arcade.color.BLACK,15) 
            
            
            arcade.draw_text("Mouse Here To Start",10,65,arcade.color.BLACK,10) 
            arcade.draw_circle_outline(50,50,10,arcade.color.BLACK)
    
            if self.mouse == 1: 
                self.set_mouse_visible(False)
                self.immuneStart = time.time()
                self.lives = 3
                self.immune = True
                self.start = 1   
            
            
    def update(self,dt):
        
        
        
        if self.start == 1:
            self.sprite_list.update()
            if self.easy == True:
                self.fireball_time = 0
                self.fireball_count = 100
                
            if self.easy == False and self.immune == True:
                self.left_down = False
        
            sprites_hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.sprite_list)
        
            for sprite in sprites_hit_list:
                if self.easy == False:
                    if self.immune == False:
                        sprite.kill()
                        self.score += 1        
                else:
                    sprite.kill()
                    self.score += 1 
                    
            enemy_hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.enemy_list)
            if self.immune == False:
                for enemy in enemy_hit_list:
        
                    self.player_sprite.alpha = .5
                    self.immuneStart = time.time()
                    self.immune = True
                    self.hit = True
                    self.lives -= 1      
            if self.immune == True:
                self.immuneTime = round(time.time() - self.immuneStart,1)
        
        
            if self.immuneTime % .5 == 0 and self.immune == True:
        
                if self.player_sprite.alpha == .5:
                    self.player_sprite.alpha = 1
        
        
                else:
                    self.player_sprite.alpha = .5
        
        
            if time.time() - self.immuneStart >= 3:
                self.immune = False
                self.hit = False
                self.player_sprite.alpha = 1
            '''
                if self.player_sprite.center_y > 25:
                    self.player_sprite.center_y -= .5  
                '''   
            for enemy in self.enemy_list:
                enemy.center_x -= enemy.dx
                if enemy.center_x <= -20:
                    enemy.center_x = SCREEN_WIDTH + 20
                    enemy.center_y = random.randrange(SCREEN_HEIGHT-20)
                    enemy.dx = random.uniform(.5,2)       
                
                    
                    
            if self.left_down == True and len(self.fireball_list) <= self.fireball_count - 1 and time.time() - self.fireball_starttime > self.fireball_time:
                self.fireball_starttime = time.time()
                fireball = arcade.Sprite("watermelon.png",.2)
                fireball.center_x = self.player_sprite.center_x + 40
                fireball.center_y = self.player_sprite.center_y 
                self.fireball_list.append(fireball) 
                
                
            for fireball in self.fireball_list:
                fireball.center_x += 4
                if fireball.center_x > SCREEN_WIDTH + 40:
                    fireball.kill()
                    break
                fireball_hit_list = arcade.check_for_collision_with_list(fireball,self.enemy_list)
                for enemy in fireball_hit_list:
                    enemy.center_x = SCREEN_WIDTH + 30
                    enemy.center_y = random.randrange(SCREEN_HEIGHT-20)
                    enemy.dx = random.uniform(.5,2)   
                    fireball.kill()
            
            self.left_down = False

    def on_mouse_motion(self,x,y,dx,dy):
        
        if x < SCREEN_WIDTH - 20 and x > 20 :
            self.player_sprite.center_x = x
        
        if y < SCREEN_HEIGHT - 25 and y > 25 :
            self.player_sprite.center_y = y
            
        if 40 < x < 60 and 40 < y < 60:
            self.mouse = 1
            
        
    def on_key_press(self,key,modifiers):
        
        if self.start < 1:
            if key == arcade.key.UP:
                self.easy = False
            if key == arcade.key.DOWN:
                self.easy = True
            
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.left_down = True
    
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT+40, "Drawing Example")
    arcade.run()
        
main()