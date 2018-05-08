import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Paddle(arcade.Sprite):
    def __init__(self, x, y, image):
        super().__init__(image)
        self.x = x
        self.y = y
        
    

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        self.set_mouse_visible(False)
        
        arcade.set_background_color(arcade.color.ASH_GREY)
        
        self.all_sprites_list = None
        
    def setup(self):
        
        self.all_sprites_list = arcade.SpriteList()
        self.player = Paddle(SCREEN_WIDTH // 2, 30, "paddle.png")
        self.all_sprites_list.append(self.player)
        
    def on_draw(self):
        arcade.start_render()        
        self.all_sprites_list.draw()
        
    def update(self,dt):
        "update"
        
        
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Bullet Demo")
    window.setup()
    arcade.run()
    
main()