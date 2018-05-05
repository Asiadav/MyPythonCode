import arcade
import random
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400


class Void:
    
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size
        self.color = arcade.color.GREY
        
    def update(self):
        "does not update"
        
    def draw(self):
        arcade.draw_rectangle_filled(self.x,self.y,self.size,self.size,self.color)

class Block:
    
    def __init__(self,x,y,size,color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        
    def update(self):
        "does not update"
        
    def draw(self):
        arcade.draw_rectangle_filled(self.x,self.y,self.size,self.size,self.color)

class MyGame(arcade.Window):
      
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        self.set_mouse_visible(False)
        
        arcade.set_background_color(arcade.color.BLACK)
        self.cord_list = []

    def setup(self):
        "setup"
        self.size = 20
        self.void_size = 24
        
        
        for i in range(0, SCREEN_WIDTH, self.void_size):
            xVal_list = []
            self.cord_list.append(xVal_list)
            
        
        for item in self.cord_list:
            for i in range(0, SCREEN_HEIGHT, self.void_size):
                yVal = 0
                item.append(yVal)           
                
        
        self.current_position_x = SCREEN_WIDTH//2
        self.current_position_y = SCREEN_HEIGHT//2
        self.x = SCREEN_WIDTH//2
        self.y = SCREEN_HEIGHT//2

        self.color = arcade.color.WHITE
        
        block = Block(self.x,self.y,self.size,self.color)
        
        self.block_list = []
        self.block_list.append(block)
        self.counter = 1
        self.counter = -1
        
        
        self.used_block_list = []
        self.done = 0
    def on_draw(self):
        arcade.start_render()
        
        for block in self.block_list:
            block.draw()
        for used in self.used_block_list:
            used.draw()
        arcade.draw_rectangle_filled(self.x,self.y,self.size,self.size,arcade.color.RED)
        
    def update(self,dt):
        "update"
        
        
        if self.done == 0:
            canMove = 1
            direction = [1,2,3,4]
            random.shuffle(direction)            
            print("loop start")
            for i in range(0,4,1):
                check = direction[i]
                canMove = 1
              
                if check == 1 and self.current_position_x - self.void_size > 0:
                    "next square is left and not on border"      
                    self.x = self.current_position_x
                    self.y = self.current_position_y                    
                    self.x -= self.void_size
                    for block in self.block_list:
                        print("self",self.x)
                        print("block",block.x)
                        if (self.x == block.x or self.x - self.void_size == block.x) and (self.y == block.y or self.y + self.void_size == block.y or self.y - self.void_size == block.y):
                            canMove = 0
                            print("left stop")
                    for block in self.used_block_list:
                        print("self",self.x)
                        print("block",block.x)
                        if (self.x == block.x or self.x - self.void_size == block.x) and (self.y == block.y or self.y + self.void_size == block.y or self.y - self.void_size == block.y):
                            canMove = 0
                            print("left stop")
                elif not(self.current_position_x - self.void_size > 0):
                    canMove = 0
                            
                    
    
                if check == 2 and self.current_position_y + self.void_size < SCREEN_HEIGHT:
                    "next square is up and not on border"
                    self.x = self.current_position_x
                    self.y = self.current_position_y                    
                    self.y += self.void_size
                    for block in self.block_list:
                        print("self",self.y)
                        print("block",block.y)                    
                        if (self.y == block.y or self.y + self.void_size == block.y) and (self.x == block.x or self.x + self.void_size == block.x or self.x - self.void_size == block.x):
                            canMove = 0            
                            print("up stop")
                    for block in self.used_block_list:
                        print("self",self.y)
                        print("block",block.y)                    
                        if (self.y == block.y or self.y + self.void_size == block.y) and (self.x == block.x or self.x + self.void_size == block.x or self.x - self.void_size == block.x):
                            canMove = 0            
                            print("up stop")
                elif not(self.current_position_y + self.void_size < SCREEN_HEIGHT):
                    canMove = 0
    
                if check == 3 and self.current_position_x + self.void_size < SCREEN_WIDTH:
                    "next square is right and not on border"
                    self.x = self.current_position_x
                    self.y = self.current_position_y                    
                    self.x += self.void_size
                    for block in self.block_list:
                        print("self",self.x)
                        print("block",block.x)                    
                        if (self.x == block.x or self.x + self.void_size == block.x) and (self.y == block.y or self.y + self.void_size == block.y or self.y - self.void_size == block.y):
                            canMove = 0            
                            print("right stop")
                    for block in self.used_block_list:
                        print("self",self.x)
                        print("block",block.x)                    
                        if (self.x == block.x or self.x + self.void_size == block.x) and (self.y == block.y or self.y + self.void_size == block.y or self.y - self.void_size == block.y):
                            canMove = 0            
                            print("right stop")
                    
                elif not( self.current_position_x + self.void_size < SCREEN_WIDTH):
                    canMove = 0
                   
                   
                if check == 4 and self.current_position_y - self.void_size > 0:
                    "next square is dowwn and not on border"
                    self.x = self.current_position_x
                    self.y = self.current_position_y                    
                    self.y -= self.void_size
                    for block in self.block_list:
                        print("self",self.y)
                        print("block",block.y)
                        if (self.y == block.y or self.y - self.void_size == block.y) and (self.x == block.x or self.x + self.void_size == block.x or self.x - self.void_size == block.x):
                            canMove = 0
                            print("up stop")
                    for block in self.used_block_list:
                        print("self",self.y)
                        print("block",block.y)
                        if (self.y == block.y or self.y - self.void_size == block.y) and (self.x == block.x or self.x + self.void_size == block.x or self.x - self.void_size == block.x):
                            canMove = 0
                            print("up stop")
                elif not(self.current_position_y - self.void_size > 0):  
                    canMove = 0
                    
                if i == 3 and canMove == 0:
                    used_up = self.block_list.pop(len(self.block_list)-1)
                    self.used_block_list.append(used_up)
                    
                if canMove == 1:
                    break
    
           # time.sleep(.5)    
    
            print("loop done\n")
            if canMove == 1:
                self.current_position_x = self.x
                self.current_position_y = self.y
                block = Block(self.current_position_x,self.current_position_y,self.size,self.color)
                self.block_list.append(block)
                self.counter = -1
                print("\n\n",len(self.block_list),"\n\n")
                
                
            
            if canMove == 0:
                #used = self.block_list.pop(len(self.block_list)-1)
                #self.used_block_list.append(used)
                print("baack")
                try:
                    self.x = self.block_list[len(self.block_list)+self.counter].x
                    self.y = self.block_list[len(self.block_list)+self.counter].y
                    self.counter -= 1
                except:
                    self.done = 1
                    
                self.current_position_x = self.x
                self.current_position_y = self.y            
    
                
            self.x = self.current_position_x
            self.y = self.current_position_y                   
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "maze maker")
    window.setup()
    arcade.run()
        
main()