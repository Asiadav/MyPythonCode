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
        
        
        self.npc1_location = []
        self.layer_list = []
        
        self.camera.change_angle = 0
        
        self.render_distance = 125
        
        self.wall = arcade.load_texture("brick_wall.jpg")
        
        """ quality settings """
        self.ray_speed = 4 #basically achieves AA
        self.res = 40      #steps in 800 range
        self.thickness = 1/15
        
        
    def raycast(self):
        
        for i in range(-400,400,self.res):
            ray = arcade.Sprite("circle.png",0.005)
            ray.angle = i//10 + self.camera.angle - 90
            ray.center_x = self.camera.center_x
            ray.center_y = self.camera.center_y
            self.rayCast_list.append(ray)
            
        while len(self.rayCast_list) > 0:
            for ray in self.rayCast_list:
                ray.center_x += math.cos(math.radians(ray.angle)) * self.ray_speed
                ray.center_y += math.sin(math.radians(ray.angle)) * self.ray_speed
                cast_hit_list = arcade.check_for_collision_with_list(ray,self.wall_list)
                if len(cast_hit_list) != 0:
                    draw_point = [ray.center_x,ray.center_y,math.sqrt((ray.center_x-self.camera.center_x) ** 2 + (ray.center_y-self.camera.center_y) ** 2),ray.angle,ray.angle,0]
                    self.draw_point_list.append(draw_point)
                    ray.kill()
                npc_hit = arcade.check_for_collision(ray,self.npc1)
                if npc_hit:
                    npc_pos = SCREEN_WIDTH//6 + (self.camera.angle - ray.angle) * 7
                    self.npc1_location.append(npc_pos)
                    
                if math.sqrt((ray.center_x-self.camera.center_x) ** 2 + (ray.center_y-self.camera.center_y) ** 2) > self.render_distance:
                    ray.kill()
            
    def draw_3d(self):
        for draw_point in self.draw_point_list:
            draw_point[3] = SCREEN_WIDTH//6 + (self.camera.angle - draw_point[4]) * 7
      
            draw_point[4] = int(200 - draw_point[2])
            
            self.layer_list.append((draw_point[2],draw_point[3],SCREEN_HEIGHT//2,self.res * 1.2,4000 / draw_point[2],(draw_point[4] - 20,draw_point[4]-20,draw_point[4]-20)))
             
            #self.layer_list.append((draw_point[2],draw_point[3],SCREEN_HEIGHT//2,700/draw_point[2]*self.res*self.thickness,5000 / draw_point[2],(draw_point[4] - 20,draw_point[4]-20,draw_point[4]-20)))

    def npc_draw(self):
        self.npc1_sprite.center_x = -50
        if len(self.npc1_location) != 0:
            self.npc1_sprite.center_x = sum(self.npc1_location)/len(self.npc1_location)
            
            distance = math.sqrt((self.npc1.center_x-self.camera.center_x) ** 2 + (self.npc1.center_y-self.camera.center_y) ** 2) 
            self.layer_list.append((distance,"npc"))
            self.npc1_location = []
    
    def draw_2d(self):   
        self.npc1.draw()
        self.wall_list.draw()
        self.camera.draw()
        self.rayCast_list.draw()        
        
    def on_draw(self):
        arcade.start_render()  
        
        arcade.draw_rectangle_filled(850,210,600,200,arcade.color.BROWN)
        arcade.draw_rectangle_filled(850,390,600,180,arcade.color.DARK_BROWN)
        
        self.npc_draw()
        
        self.layer_list.sort()
        for i in range(len(self.layer_list)-1,-1,-1):
            if self.layer_list[i][1] == "npc":
                center_x = self.npc1_sprite.center_x
                self.npc1_sprite = arcade.Sprite("Dragon.png",5/self.layer_list[i][0])
                self.npc1_sprite.center_y = SCREEN_HEIGHT//2        
                self.npc1_sprite.center_x = center_x
                self.npc1_sprite.draw()
                
            else:
                
                arcade.draw_texture_rectangle(self.layer_list[i][1],self.layer_list[i][2],self.layer_list[i][3],self.layer_list[i][4],self.wall)
                           
                #arcade.draw_rectangle_filled(self.layer_list[i][1],self.layer_list[i][2],self.layer_list[i][3],self.layer_list[i][4],(200.0000001,200,200,200))
                color = 100 #int(self.layer_list[i][4])
                alpha = int(self.layer_list[i][0]*2)
                print(alpha)
                
                arcade.draw_rectangle_filled(self.layer_list[i][1],self.layer_list[i][2],self.layer_list[i][3],self.layer_list[i][4],(color,color,color,alpha))
                
                
        self.layer_list = []            

        self.draw_3d()
        
        self.draw_2d()
        
        self.draw_point_list = []
        
        arcade.draw_rectangle_outline(850,300,600,380,arcade.color.GRAY, 100)
        
        
        
    def update(self,dt):
        "update" 
        
        if time.time() - self.raycast_start > 0.01:
            self.raycast_start = time.time()
            self.raycast()
        
        if self.W_pressed:
            self.camera.change_y = math.sin(math.radians(self.camera.angle - 90)) * 1.5
            self.camera.change_x = math.cos(math.radians(self.camera.angle - 90)) * 1.5
        if self.S_pressed:
            self.camera.change_y = -math.sin(math.radians(self.camera.angle - 90)) * 1.5
            self.camera.change_x = -math.cos(math.radians(self.camera.angle - 90)) * 1.5      
        if self.A_pressed:
            self.camera.change_y = math.sin(math.radians(self.camera.angle )) * 1.5
            self.camera.change_x = math.cos(math.radians(self.camera.angle )) * 1.5
        if self.D_pressed:
            self.camera.change_y = -math.sin(math.radians(self.camera.angle )) * 1.5
            self.camera.change_x = -math.cos(math.radians(self.camera.angle )) * 1.5
        
        
        self.camera.center_x += self.camera.change_x
        wall_hit_list = arcade.check_for_collision_with_list(self.camera,self.wall_list)
        npc_hit_list = arcade.check_for_collision_with_list(self.camera,self.npc_list)        
        if len(wall_hit_list) != 0 or len(npc_hit_list) != 0:
            self.camera.center_x -= self.camera.change_x
        
        self.camera.center_y += self.camera.change_y
        wall_hit_list = arcade.check_for_collision_with_list(self.camera,self.wall_list)
        npc_hit_list = arcade.check_for_collision_with_list(self.camera,self.npc_list)     
        if len(wall_hit_list) != 0 or len(npc_hit_list) != 0:
            self.camera.center_y -= self.camera.change_y          
        
        self.camera.angle += self.camera.change_angle
    def on_key_press(self,key,modifiers):

        if key == arcade.key.A:
            self.A_pressed = True
 
            
        if key == arcade.key.D:
            self.D_pressed = True    

        
        if key == arcade.key.W:
            self.W_pressed = True
            
        if key == arcade.key.S:
            self.S_pressed = True    
 
        if key == arcade.key.RIGHT:
            self.camera.change_angle = -5
        if key == arcade.key.LEFT:
            self.camera.change_angle = 5
            
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
        
        if key == arcade.key.RIGHT:
            self.camera.change_angle = 0
        if key == arcade.key.LEFT:
            self.camera.change_angle = 0
            
    def on_mouse_motion(self,x,y,dx,dy):
        
        #self.rayCast_list = arcade.SpriteList()
        self.camera.angle -= dx / 2
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