import arcade
import random
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Coin(arcade.AnimatedTimeSprite):
    def __init__(self, x, y):
        super().__init__(self)
        self.center_x = x
        self.center_y = y
        self.scale = 0.5
       
        self.textures = []
        self.textures.append(arcade.load_texture("gold_1.png"))
        self.textures.append(arcade.load_texture("gold_2.png"))
        self.textures.append(arcade.load_texture("gold_3.png"))
        self.textures.append(arcade.load_texture("gold_4.png"))
        self.textures.append(arcade.load_texture("gold_3.png", mirrored = True))
        self.textures.append(arcade.load_texture("gold_2.png", mirrored = True))
        self.textures.append(arcade.load_texture("gold_1.png", mirrored = True))       

class Jim(arcade.AnimatedWalkingSprite):
    def __init__(self, x, y,):
        super().__init__(self)
        self.center_x = x
        self.center_y = y
        self.scale = 0.3
        
        self.stand_right_textures = []
        self.stand_right_textures.append(arcade.load_texture("walking04.png"))
        
        self.walk_right_textures = []
        self.walk_right_textures.append(arcade.load_texture("walking01.png"))
        self.walk_right_textures.append(arcade.load_texture("walking02.png"))
        self.walk_right_textures.append(arcade.load_texture("walking03.png"))
        self.walk_right_textures.append(arcade.load_texture("walking04.png"))
        self.walk_right_textures.append(arcade.load_texture("walking05.png"))
        self.walk_right_textures.append(arcade.load_texture("walking06.png"))
        self.walk_right_textures.append(arcade.load_texture("walking07.png"))
        self.walk_right_textures.append(arcade.load_texture("walking08.png"))
        
        self.stand_left_textures = []
        self.stand_left_textures.append(arcade.load_texture("walking04.png", mirrored = True))
        
        self.walk_left_textures = []
        self.walk_left_textures.append(arcade.load_texture("walking01.png", mirrored = True))
        self.walk_left_textures.append(arcade.load_texture("walking02.png", mirrored = True))
        self.walk_left_textures.append(arcade.load_texture("walking03.png", mirrored = True))
        self.walk_left_textures.append(arcade.load_texture("walking04.png", mirrored = True))
        self.walk_left_textures.append(arcade.load_texture("walking05.png", mirrored = True))
        self.walk_left_textures.append(arcade.load_texture("walking06.png", mirrored = True))
        self.walk_left_textures.append(arcade.load_texture("walking07.png", mirrored = True))
        self.walk_left_textures.append(arcade.load_texture("walking08.png", mirrored = True))        
        self.texture_change_distance = 30
        

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        self.set_mouse_visible(False)
        
        arcade.set_background_color(arcade.color.ASH_GREY)
        
        self.all_sprites_list = None
        
        self.coin_list = None
        
    def setup(self):
        
        self.all_sprites_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        
        self.player = Jim(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
        self.all_sprites_list.append(self.player)
        
        self.W = False
        self.A = False
        self.S = False
        self.D = False
        
        
    def on_draw(self):
        arcade.start_render()        
        self.all_sprites_list.draw()
        
        
    def update(self,dt):
        "update"
        self.all_sprites_list.update()
        
        if self.player.center_x > SCREEN_WIDTH + 30:
            self.player.center_x = -30
        if self.player.center_x < -30:
            self.player.center_x = SCREEN_WIDTH + 30
        if self.player.center_y > SCREEN_HEIGHT + 30:
            self.player.center_y = -30
        if self.player.center_y < -30:
            self.player.center_y = SCREEN_HEIGHT + 30
        
        coin_hit_list = arcade.check_for_collision_with_list(self.player,self.coin_list)
        for coin in coin_hit_list:
            coin.kill()
            
            
            
            
        if len(self.coin_list) < 10:
            coin = Coin(random.randrange(SCREEN_WIDTH), random.randrange(SCREEN_HEIGHT))
    
            self.coin_list.append(coin)
            self.all_sprites_list.append(coin)
        
        self.all_sprites_list.update_animation()
        
        self.player.center_x += self.player.change_x
    def on_key_press(self, key, modifiers):
        
        if key == arcade.key.A:
            self.A = True
            
        if key == arcade.key.D:
            self.D = True
        if key == arcade.key.W:
            self.W = True
        if key == arcade.key.S:
            self.S = True
            
            
        if self.W:
            self.player.change_y = 5
        if self.A:
            self.player.change_x = -5
        if self.S:
            self.player.change_y = -5
        if self.D:
            self.player.change_x = 5
            
            
    def on_key_release(self, key, modifiers):
        
        if key == arcade.key.A:
            self.A = False        
        if key == arcade.key.A and self.D == False:
            self.player.change_x = 0
            
        if key == arcade.key.D:
            self.D = False
        if key == arcade.key.D and self.A == False:
            self.player.change_x = 0
            
        if key == arcade.key.W or key == arcade.key.S:
            self.player.change_y = 0

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Animation")
    window.setup()
    arcade.run()
    
main()