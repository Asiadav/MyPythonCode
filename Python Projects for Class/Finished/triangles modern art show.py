import arcade
import random
import time
global width
global height
global ticker
ticker = 0
width = 1000
height = 680


class Triangles:
    
    def __init__(self,x,y,size,color):
        self.x = x
        
        self.y = y
        
        self.size = size
        
        self.color = color
        
        self.x_range = width
        
        self.y_range = height


        
    def draw(self):       
        
        arcade.draw_triangle_filled(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.color)
        
    def update(self):
        global width
        global height
        global ticker
        
        self.color = (random.randrange(255),random.randrange(255),random.randrange(255))
        
        randModX = random.randrange(width)
        randModY = random.randrange(height)
        
        
        self.x1 = random.randint(randModX-self.size,randModX+self.size)
        self.x2 = random.randint(randModX-self.size,randModX+self.size)
        self.x3 = random.randint(randModX-self.size,randModX+self.size)
        
        
        self.y1 = random.randint(randModY-self.size,randModY+self.size)
        self.y2 = random.randint(randModY-self.size,randModY+self.size)
        self.y3 = random.randint(randModY-self.size,randModY+self.size)        
        
        ticker += 1
        
        if ticker > 200:
            time.sleep(.1)
        
class MyGame(arcade.Window):
      
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        
        
        x = random.randrange(width)
        y = random.randrange(height)
        size = 200
        
        color = (random.randrange(255),random.randrange(255),random.randrange(255))
        
        
        self.triangles = Triangles(x,y,size,color)
        
        #arcade.start_render()
        
    def on_draw(self):
        

        self.triangles.draw()
    
    def update(self,delta_time):
            self.triangles.update()

def main():
    window = MyGame(width, height, "Abstact art")
    arcade.run()
        
main()