import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(arcade.Sprite):
    def __init__(self,image,scale):
        super().__init__(image,scale)
        
    
class Wall(arcade.Sprite):
    def __init__(self,image,scale):
        super().__init__(image,scale)    
    


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
                
        arcade.set_background_color(arcade.color.ASH_GREY)
        
        self.wall_list = None
        self.player_list = None
        
        self.player = None
        
        self.physics_engine = None
        
    def setup(self):
        "setup"
        
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        
        self.player = Player("player.png", 1)
        self.player.center_x = 50
        self.player.center_y = 50
        self.player_list.append(self.player)
        
        self.wall = Wall("crate.png", 1)
        
    def on_draw(self):
        "draw"
        
        arcade.start_render()
        self.player_list.draw()
        self.wall_list.draw()
        
    def update(self,dt):
        "update"
        
        
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "physics engine")
    window.setup()
    arcade.run()
    
main()