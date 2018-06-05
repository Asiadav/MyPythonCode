import arcade
import math
import time


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600


class Paddle(arcade.Sprite):
    def __init__(self, x, y, image):
        super().__init__(image)
        self.x = x
        self.y = y
        
    

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        self.set_mouse_visible(True)
        
        arcade.set_background_color(arcade.color.WHITE)
        
        
    def setup(self):
        
        self.wall_list = arcade.SpriteList()
        self.npc_list = arcade.SpriteList()
        
        wall_coord_list = [(135,300,90),(370,300,90),(320,350,0),(60,350,0),(10,425,90),(135,425,90),(10,525,90),(60,600,0),(300,600,0),(375,540,90),(265,175,90),(210,125,0),(160,50,90),(10,175,90),(10,50,90),(320,225,0),(85,225,0),(85,10,0),(445,350,0),(445,490,0),(635,420,90),(505,540,90),(565,610,0),(635,300,90),(585,230,0),(375,160,90),(510,174,90),(510,62,90),(434,8,0),(285,80,315),(346,16,135),(675,440,135),(695,610,180),(748,562,135),(714,336,90),(850,520,180),(920,470,90),(758,272,180),(918,348,90),(864,272,180),(112,668,90),(246,672,90),(184,856,180),(128,912,90),(58,728,180),(8,802,90),(8,920,90),(8,1004,90),(60,1076,0),(184,1078,0),(184,1074,0),(260,1020,90),(260,906,90),(332,852,0),(312,720,0),(442,816,135),(546,650,225),(592,750,90),(485,830,90),(590,874,90),(548,978,315),(462,986,225),(380,908,225)]
        
        for coord in wall_coord_list:
            wall = arcade.Sprite("BR.png",0.02)
            wall.center_x = coord[0] // 4
            wall.center_y = coord[1] // 4
            wall.angle = coord[2]
            self.wall_list.append(wall)            

        self.npc1 = arcade.Sprite("circle.png",0.0125)
        self.npc1.center_x = 330 // 4
        self.npc1.center_y = 285 // 4
        self.npc_list.append(self.npc1)
        
        self.npc1_sprite = arcade.Sprite("Dragon.png",0.075)
        self.npc1_sprite.center_y = SCREEN_HEIGHT//2
        self.npc1_sprite.center_x = -50
        
        self.camera = arcade.Sprite("Triangle.png",0.0025)
        self.camera.center_x = 85 // 4
        self.camera.center_y = 85 // 4
        self.camera.angle = 0
        
        self.rayCast_list = arcade.SpriteList()
        
        self.draw_point_list = []
        self.raycast_start = 0
        
        self.W_pressed = False
        self.A_pressed = False
        self.S_pressed = False
        self.D_pressed = False
        
        
        self.AA = False
        self.npc1_location = []
        self.layer_list = []
        
        """ quality settings """
        self.ray_speed = 2 #basically achieves AA
        self.res = 30      #steps in 800 range
        self.thickness = 1/15
        

        self.new_wall = arcade.Sprite("BR.png",0.02)
        self.new_wall.center_x = 375//4
        self.new_wall.center_y = 540//4
        self.new_wall.angle = 90
        self.x = 375
        self.y = 540
        


    def on_draw(self):
        arcade.start_render()  
        
        arcade.draw_rectangle_filled(850,210,600,200,arcade.color.BROWN)
        arcade.draw_rectangle_filled(850,390,600,180,arcade.color.DARK_BROWN)
  
        self.npc1.draw()
        self.wall_list.draw()
        self.camera.draw()
        self.new_wall.draw()
        
                
        arcade.draw_rectangle_outline(850,300,600,380,arcade.color.GRAY, 100)
        
        
        
    def update(self,dt):
        "update" 
        print(self.x,self.y,self.new_wall.angle)
        

    def on_key_press(self,key,modifiers):

        if key == arcade.key.A:
            self.A_pressed = True
            self.new_wall.center_x -= 10/4
            self.x -= 10
        if key == arcade.key.D:
            self.D_pressed = True    
            self.new_wall.center_x += 10/4
            self.x += 10
        
        if key == arcade.key.W:
            self.W_pressed = True
            self.new_wall.center_y += 10/4
            self.y += 10           
        if key == arcade.key.S:
            self.S_pressed = True    
            self.new_wall.center_y -= 10/4
            self.y -= 10 
            
        if key == arcade.key.R:
            self.new_wall.angle += 45
            if self.new_wall.angle>360:
                self.new_wall.angle = 0
            
    def on_key_release(self,key,modifiers):
        
        if key == arcade.key.W:
            self.W_pressed = False
 
            
        if key == arcade.key.A:
            self.A_pressed = False

        if key == arcade.key.S:
            self.S_pressed = False

            
        if key == arcade.key.D:
            self.D_pressed = False
            
    def on_mouse_press(self, x, y, button, modifiers):
        self.new_wall.center_x = x
        self.new_wall.center_y = y
        self.x = x * 4
        self.y = y * 4

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "3D Test")
    window.setup()
    arcade.run()
    
main()