import arcade
import random

COIN_COUNT = 50
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400


class MyGame(arcade.Window):
      
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        self.set_mouse_visible(False)
        
        arcade.set_background_color(arcade.color.ASH_GREY)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        
        self.score = 0
        self.player_sprite = arcade.Sprite("character.png",.7)
        
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        
        self.player_list.append(self.player_sprite)
        
        for i in range(COIN_COUNT):
            coin = arcade.Sprite("coin_01.png",.3)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            print(coin.center_y)
            self.coin_list.append(coin)
            
    def on_draw(self):
        
        arcade.start_render()

        self.player_list.draw()
        self.coin_list.draw()
        
        output = f"score: {self.score}"
        arcade.draw_text(output,10,20,arcade.color.WHITE,14)
        

    def on_mouse_motion(self,x,y,dx,dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
        
        
    def update(self,dt):
        self.coin_list.update()
        
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.coin_list)
    
        for coin in coins_hit_list:
            coin.kill()
            self.score += 1
        
        
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite test")
    window.setup()
    arcade.run()
        
main()