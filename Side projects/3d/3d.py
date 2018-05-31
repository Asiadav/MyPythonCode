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
        
        self.wall1 = arcade.Sprite("BR.png",0.08)
        self.wall1.center_x = 85
        self.wall1.center_y = 10
        self.wall1.angle = 0
        self.wall_list.append(self.wall1)
        
        self.wall2 = arcade.Sprite("BR.png",0.08)
        self.wall2.center_x = 85
        self.wall2.center_y = 225
        self.wall2.angle = 0
        self.wall_list.append(self.wall2)
        
        self.wall2 = arcade.Sprite("BR.png",0.08)
        self.wall2.center_x = 210
        self.wall2.center_y = 225
        self.wall2.angle = 0
        self.wall_list.append(self.wall2)        
        
        self.wall3 = arcade.Sprite("BR.png",0.08)
        self.wall3.center_x = 10
        self.wall3.center_y = 50
        self.wall3.angle = 90
        self.wall_list.append(self.wall3)   
        
        self.wall3 = arcade.Sprite("BR.png",0.08)
        self.wall3.center_x = 10
        self.wall3.center_y = 175
        self.wall3.angle = 90
        self.wall_list.append(self.wall3)        
        
        self.wall4 = arcade.Sprite("BR.png",0.08)
        self.wall4.center_x = 160
        self.wall4.center_y = 50
        self.wall4.angle = 90
        self.wall_list.append(self.wall4) 
        
        self.wall4 = arcade.Sprite("BR.png",0.08)
        self.wall4.center_x = 210
        self.wall4.center_y = 125
        self.wall4.angle = 0
        self.wall_list.append(self.wall4) 
        
        self.wall2 = arcade.Sprite("BR.png",0.08)
        self.wall2.center_x = 265
        self.wall2.center_y = 175
        self.wall2.angle = 90
        self.wall_list.append(self.wall2)        
        '''
        coord_list = [(10,10),(60,10),(110,10),(160,10),(10,60),(10,110),(10,160),(60,160),(110,160),(160,160),(160,60),(160,110)] 
                             
        for coord in coord_list:
            wall = arcade.Sprite("circle.png",.03)
            wall.center_x = coord[0]
            wall.center_y = coord[1]
            self.wall_list.append(wall)
        '''
        self.camera = arcade.Sprite("Triangle.png",0.01)
        self.camera.center_x = 85
        self.camera.center_y = 85
        
        self.rayCast_list = arcade.SpriteList()
        
        self.draw_point_list = []
        self.raycast_start = 0
        
        self.W_pressed = False
        self.A_pressed = False
        self.S_pressed = False
        self.D_pressed = False
        
        self.res = 5
        
    def raycast(self):
        
        for i in range(-45,45,self.res):
            ray = arcade.Sprite("circle.png",0.01)
            ray.angle = i + self.camera.angle - 90
            ray.center_x = self.camera.center_x
            ray.center_y = self.camera.center_y
            self.rayCast_list.append(ray)
        
    def draw_3d(self):
    
        for draw_point in self.draw_point_list:
            draw_point[3] = SCREEN_WIDTH//8 + (self.camera.angle - draw_point[3]) * 6
      
            draw_point[4] = int(200 - draw_point[2])
            arcade.draw_rectangle_filled(draw_point[3],SCREEN_HEIGHT//2, 1500/draw_point[2]*self.res, 20000 / draw_point[2], (draw_point[4],draw_point[4],draw_point[4],))
            #arcade.draw_rectangle_filled(drawX,SCREEN_HEIGHT//2, 15, 30000 / draw_point[2], arcade.color.BLACK)
        
        AA_list = []
        for i in range(len(self.draw_point_list)-1):
            print("comparing:", self.draw_point_list[i][2])
            print("to:", self.draw_point_list[i + 1][2])
            
            if -10 < self.draw_point_list[i][0] - self.draw_point_list[i + 1][0] < 10 and -30 < self.draw_point_list[i][1] - self.draw_point_list[i + 1][1] < 30 and -40 < self.draw_point_list[i][3] - self.draw_point_list[i + 1][3] < 40:
                arcade.draw_rectangle_filled((self.draw_point_list[i][3] + self.draw_point_list[i+1][3])/2,SCREEN_HEIGHT//2, (1500/self.draw_point_list[i][2]*self.res + 1500/self.draw_point_list[i][2]*self.res)/2, (20000 / self.draw_point_list[i][2] + 20000/self.draw_point_list[i][2])/2, arcade.color.RED)
                
                x = (self.draw_point_list[i][3] + self.draw_point_list[i+1][3])/2 - (1500/self.draw_point_list[i][2]*self.res + 1500/self.draw_point_list[i][2]*self.res)/4
                
                y = (20000 / self.draw_point_list[i][2] + 20000/self.draw_point_list[i][2])/4
                
                AA_list.append((x,y))

                
            elif -10 < self.draw_point_list[i][1] - self.draw_point_list[i + 1][1] < 10 and -30 < self.draw_point_list[i][0] - self.draw_point_list[i + 1][0] < 30 and -40 < self.draw_point_list[i][3] - self.draw_point_list[i + 1][3] < 40:
                arcade.draw_rectangle_filled((self.draw_point_list[i][3] + self.draw_point_list[i+1][3])/2,SCREEN_HEIGHT//2, (1500/self.draw_point_list[i][2]*self.res + 1500/self.draw_point_list[i][2]*self.res)/2, (20000 / self.draw_point_list[i][2] + 20000/self.draw_point_list[i][2])/2, arcade.color.RED)  
                
                x = (self.draw_point_list[i][3] + self.draw_point_list[i+1][3])/2 - (1500/self.draw_point_list[i][2]*self.res + 1500/self.draw_point_list[i][2]*self.res)/4
                
                y = (20000 / self.draw_point_list[i][2] + 20000/self.draw_point_list[i][2])/4
                
                AA_list.append((x,y))
              
                
                #(self.draw_point_list[i][4],self.draw_point_list[i][4],self.draw_point_list[i][4]))   
        
        AA_list.sort()

        if len(AA_list) > 1:
            coord_tuple = ((AA_list[0][0], SCREEN_HEIGHT//2 + AA_list[0][1]) , (AA_list[0][0], SCREEN_HEIGHT//2 - AA_list[0][1]) , (AA_list[0][0], SCREEN_HEIGHT//2 + AA_list[len(AA_list)-1][1]) , (AA_list[len(AA_list)-1][0], SCREEN_HEIGHT//2 - AA_list[len(AA_list)-1][1]))
            arcade.draw_polygon_filled(coord_tuple,(10,10,10))
                
        self.draw_point_list = []

        
    def on_draw(self):
        arcade.start_render()  
        
        arcade.draw_rectangle_filled(700,210,600,200,arcade.color.BROWN)
        arcade.draw_rectangle_filled(700,390,600,180,arcade.color.DARK_BROWN)
        
        self.draw_3d()
        
        self.wall_list.draw()
        self.camera.draw()
        self.rayCast_list.draw()
        
        arcade.draw_rectangle_outline(700,300,600,380,arcade.color.GRAY, 100)
        
        
        
    def update(self,dt):
        "update" 
        
        if time.time() - self.raycast_start > 0.01:
            self.raycast_start = time.time()
            self.raycast()
        
        for ray in self.rayCast_list:
            ray.center_x += math.cos(math.radians(ray.angle)) * 10
            ray.center_y += math.sin(math.radians(ray.angle)) * 10
            cast_hit_list = arcade.check_for_collision_with_list(ray,self.wall_list)
            if len(cast_hit_list) != 0:
                draw_point = [ray.center_x,ray.center_y,math.sqrt((ray.center_x-self.camera.center_x) ** 2 + (ray.center_y-self.camera.center_y) ** 2),ray.angle,0,0]
                self.draw_point_list.append(draw_point)
                ray.kill()
        
        
        if self.W_pressed:
            self.camera.change_y = math.sin(math.radians(self.camera.angle - 90)) * 2
            self.camera.change_x = math.cos(math.radians(self.camera.angle - 90)) * 2
        if self.S_pressed:
            self.camera.change_y = -math.sin(math.radians(self.camera.angle - 90)) * 2
            self.camera.change_x = -math.cos(math.radians(self.camera.angle - 90)) * 2         
        if self.A_pressed:
            self.camera.change_y = math.sin(math.radians(self.camera.angle )) * 2
            self.camera.change_x = math.cos(math.radians(self.camera.angle )) * 2
        if self.D_pressed:
            self.camera.change_y = -math.sin(math.radians(self.camera.angle )) * 2
            self.camera.change_x = -math.cos(math.radians(self.camera.angle )) * 2
        
        self.camera.center_x += self.camera.change_x
    
        wall_hit_list = arcade.check_for_collision_with_list(self.camera,self.wall_list)
        if len(wall_hit_list) != 0:
            self.camera.center_x -= self.camera.change_x
        
        self.camera.center_y += self.camera.change_y
        
        wall_hit_list = arcade.check_for_collision_with_list(self.camera,self.wall_list)
        if len(wall_hit_list) != 0:
            self.camera.center_y -= self.camera.change_y          
            
            
    def on_key_press(self,key,modifiers):

        if key == arcade.key.A:
            self.A_pressed = True
 
            
        if key == arcade.key.D:
            self.D_pressed = True    

        
        if key == arcade.key.W:
            self.W_pressed = True
            
        if key == arcade.key.S:
            self.S_pressed = True    
 
            
    def on_key_release(self,key,modifiers):
        
        if key == arcade.key.W:
            self.W_pressed = False
            self.camera.change_y = 0
            self.camera.change_x = 0
            
        if key == arcade.key.A:
            self.A_pressed = False
            self.camera.change_x = 0
            self.camera.change_y = 0
            
        if key == arcade.key.S:
            self.S_pressed = False
            self.camera.change_y = 0
            self.camera.change_x = 0
            
        if key == arcade.key.D:
            self.D_pressed = False
            self.camera.change_x = 0           
            self.camera.change_y = 0
            
    def on_mouse_motion(self,x,y,dx,dy):
        
        #self.rayCast_list = arcade.SpriteList()
        self.camera.angle -= dx / 1.5
        
        #self.camera.angle = math.degrees(math.atan2((self.camera.center_y - y),(self.camera.center_x - x))) -90          
        
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "3D Test")
    window.setup()
    arcade.run()
    
main()