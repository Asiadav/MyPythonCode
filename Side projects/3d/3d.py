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
        self.wall2.center_x = 320
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
        
        wall_coord_list = [(135,300,90),(370,300,90),(320,350,0),(60,350,0),(10,425,90),(135,425,90),(10,525,90),(60,600,0),(180,600,0),(300,600,0),(375,540,90),(375,420,90)]
        
        for coord in wall_coord_list:
            wall = arcade.Sprite("BR.png",0.08)
            wall.center_x = coord[0]
            wall.center_y = coord[1]
            wall.angle = coord[2]
            self.wall_list.append(wall)            

        self.npc1 = arcade.Sprite("circle.png",0.05)
        self.npc1.center_x = 310
        self.npc1.center_y = 285
        
        self.npc1_sprite = arcade.Sprite("Dragon.png",0.3)
        self.npc1_sprite.center_y = SCREEN_HEIGHT//2
        self.npc1_sprite.center_x = -50
        
        self.camera = arcade.Sprite("Triangle.png",0.01)
        self.camera.center_x = 85
        self.camera.center_y = 85
        self.camera.angle = 0
        
        self.rayCast_list = arcade.SpriteList()
        
        self.draw_point_list = []
        self.raycast_start = 0
        
        self.W_pressed = False
        self.A_pressed = False
        self.S_pressed = False
        self.D_pressed = False
        
        self.res = 5
        
        self.raycast()
        self.AA = False
        self.npc1_location = []
        self.layer_list = []
        
    def raycast(self):
        
        for i in range(-45,45,self.res):
            ray = arcade.Sprite("circle.png",0.005)
            ray.angle = i + self.camera.angle - 90
            ray.center_x = self.camera.center_x
            ray.center_y = self.camera.center_y
            self.rayCast_list.append(ray)
            
    def draw_3d(self):
        for draw_point in self.draw_point_list:
            draw_point[3] = SCREEN_WIDTH//4 + (self.camera.angle - draw_point[4]) * 6
      
            draw_point[4] = int(200 - draw_point[2])
            
            
            #arcade.draw_rectangle_filled(draw_point[3],SCREEN_HEIGHT//2, 1500/draw_point[2]*self.res, 25000 / draw_point[2], (draw_point[4] + 10,draw_point[4]+10,draw_point[4]+10))
            
            self.layer_list.append((draw_point[2],draw_point[3],SCREEN_HEIGHT//2,1500/draw_point[2]*self.res,25000 / draw_point[2],(draw_point[4] + 10,draw_point[4]+10,draw_point[4]+10)))
            
            #arcade.draw_rectangle_filled(drawX,SCREEN_HEIGHT//2, 15, 30000 / draw_point[2], arcade.color.BLACK)
        
        AA_list = []
        if self.AA:
            for i in range(len(self.draw_point_list)-1):
        
                if -5 < self.draw_point_list[i][0] - self.draw_point_list[i + 1][0] < 5 and -20 < self.draw_point_list[i][1] - self.draw_point_list[i + 1][1] < 20 and -10 < self.draw_point_list[i][4] - self.draw_point_list[i + 1][4] < 10:
                    arcade.draw_rectangle_filled((self.draw_point_list[i][3] + self.draw_point_list[i+1][3])/2,SCREEN_HEIGHT//2, (1400/self.draw_point_list[i][2]*self.res + 1500/self.draw_point_list[i][2]*self.res)/2, (20000 / self.draw_point_list[i][2] + 20000/self.draw_point_list[i][2])/2, arcade.color.RED)
        
                    x = (self.draw_point_list[i][3] + self.draw_point_list[i+1][3])/2
        
                    y = (20000 / self.draw_point_list[i][2] + 20000/self.draw_point_list[i][2])/3
        
                    AA_list.append((x,y))
        
        
                elif -5 < self.draw_point_list[i][1] - self.draw_point_list[i + 1][1] < 5 and -20 < self.draw_point_list[i][0] - self.draw_point_list[i + 1][0] < 20 and -10 < self.draw_point_list[i][4] - self.draw_point_list[i + 1][4] < 10:
                    arcade.draw_rectangle_filled((self.draw_point_list[i][3] + self.draw_point_list[i+1][3])/2,SCREEN_HEIGHT//2, (1500/self.draw_point_list[i][2]*self.res + 1500/self.draw_point_list[i][2]*self.res)/2, (20000 / self.draw_point_list[i][2] + 20000/self.draw_point_list[i][2])/2, arcade.color.RED)  
        
                    x = (self.draw_point_list[i][3] + self.draw_point_list[i+1][3])/2
                    y = (20000 / self.draw_point_list[i][2] + 20000/self.draw_point_list[i][2])/3
        
                    AA_list.append((x,y))
        
                if abs(self.draw_point_list[i][0] - self.draw_point_list[i + 1][0]) < 10 and abs(self.draw_point_list[i][1] - self.draw_point_list[i + 1][1]) < 10 and abs(self.draw_point_list[i][0] - self.draw_point_list[i - 1][0]) < 10 and abs(self.draw_point_list[i][1] - self.draw_point_list[i - 1][1]) < 10:
        
                    arcade.draw_rectangle_filled(self.draw_point_list[i][3],SCREEN_HEIGHT//2, 1500/self.draw_point_list[i][2]*self.res, 20000 / self.draw_point_list[i][2], arcade.color.BLUE)
        
                    #(self.draw_point_list[i][4],self.draw_point_list[i][4],self.draw_point_list[i][4]))           
        
        AA_list.sort()

        if len(AA_list) > 1 and self.AA:
       
            coord_tuple = ((AA_list[0][0], SCREEN_HEIGHT//2 + AA_list[0][1]) , (AA_list[0][0], SCREEN_HEIGHT//2 - AA_list[0][1]) , (AA_list[len(AA_list)-1][0], SCREEN_HEIGHT//2 - AA_list[len(AA_list)-1][1]) , (AA_list[len(AA_list)-1][0], SCREEN_HEIGHT//2 + AA_list[len(AA_list)-1][1]))
            arcade.draw_polygon_filled(coord_tuple,(10,10,10))
            

       
        
        
    def npc_draw(self):
        self.npc1_sprite.center_x = -50
        if len(self.npc1_location) != 0:
            self.npc1_sprite.center_x = sum(self.npc1_location)/len(self.npc1_location)
            self.npc1_sprite.draw()
            self.npc1_location = []
    
        
        
        
    def on_draw(self):
        arcade.start_render()  
        
        arcade.draw_rectangle_filled(850,210,600,200,arcade.color.BROWN)
        arcade.draw_rectangle_filled(850,390,600,180,arcade.color.DARK_BROWN)
        
        #add the npc to the list, and give npc distance
        #optimize
        #basically works
        
        self.layer_list.sort()
        for i in range(len(self.layer_list)-1,0,-1):
            arcade.draw_rectangle_filled(self.layer_list[i][1],self.layer_list[i][2],self.layer_list[i][3],self.layer_list[i][4],self.layer_list[i][5])
        self.layer_list = []            

        self.draw_3d()
        '''
        self.npc_draw()
        '''
        self.npc1.draw()
        self.wall_list.draw()
        self.camera.draw()
        self.rayCast_list.draw()
        
        self.draw_point_list = []
        
        arcade.draw_rectangle_outline(850,300,600,380,arcade.color.GRAY, 100)
        
        
        
    def update(self,dt):
        "update" 
        
        if time.time() - self.raycast_start > 0.01:
            self.raycast_start = time.time()
            self.raycast()
        '''
        if len(self.rayCast_list) == 0:
            self.raycast_start = time.time()
            
            self.raycast()
        '''    
        for ray in self.rayCast_list:
            ray.center_x += math.cos(math.radians(ray.angle)) * 10
            ray.center_y += math.sin(math.radians(ray.angle)) * 10
            cast_hit_list = arcade.check_for_collision_with_list(ray,self.wall_list)
            if len(cast_hit_list) != 0:
                draw_point = [ray.center_x,ray.center_y,math.sqrt((ray.center_x-self.camera.center_x) ** 2 + (ray.center_y-self.camera.center_y) ** 2),ray.angle,ray.angle,0]
                self.draw_point_list.append(draw_point)
                ray.kill()
            npc_hit_list = arcade.check_for_collision(ray,self.npc1)
            if npc_hit_list and math.sqrt((ray.center_x-self.camera.center_x) ** 2 + (ray.center_y-self.camera.center_y) ** 2) < 80:
                npc_pos = SCREEN_WIDTH//4 + (self.camera.angle - ray.angle) * 6
                self.npc1_location.append(npc_pos)
        
        
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
        '''
        if self.camera.angle > 360:
            self.camera.angle = 0
        elif self.camera.angle < 0:
            self.camera.angle = 360
        '''
        #self.camera.angle = math.degrees(math.atan2((self.camera.center_y - y),(self.camera.center_x - x))) -90          
        
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "3D Test")
    window.setup()
    arcade.run()
    
main()