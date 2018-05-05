import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400


class MyGame(arcade.Window):
      
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        self.set_mouse_visible(False)
        
        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        self.square_list = arcade.SpriteList()
        

        square_sprite = arcade.Sprite("square.jpg",.2)
        
        square_sprite.center_x = SCREEN_WIDTH / 4
        square_sprite.center_y = SCREEN_HEIGHT - 25
        self.square_list.append(square_sprite)
        
        self.counter = 0
        self.overtop = []
        
    def on_draw(self):
        
        arcade.start_render()

        self.square_list.draw()
        
        
    def update(self,dt):
        
        self.square_list.update()
        counterTime = 97
        collision_number = 0
        self.counter += 1
        
        if self.counter % counterTime == 0 and self.counter < counterTime * 15:
            square_sprite1 = arcade.Sprite("square.jpg",.2)
            square_sprite1.center_x = random.randrange(15,SCREEN_WIDTH-15)
            square_sprite1.center_y = SCREEN_HEIGHT - 15
            self.square_list.append(square_sprite1)
        """
        if self.counter == 100 or self.counter == 200 or self.counter == 300:
            square_sprite1 = arcade.Sprite("square.jpg",.2)
            square_sprite1.center_x = SCREEN_WIDTH / 2
            square_sprite1.center_y = SCREEN_HEIGHT - 15
            self.square_list.append(square_sprite1)          
        """  
            
        hitListCount = 0
        overtopCount = 0
        self.overtop = []
        hitList = []
        for item in self.square_list: 
            dy = 5
            item = self.square_list.pop()
            hl = arcade.check_for_collision_with_list(item,self.square_list)
            hitList.append(hl)
            self.overtop.append(0)
            #print(hitList)
            
            for x in self.square_list:
                
                
                #print("square bottom", item.bottom)
                #print("other square top",x.top)
                if item.bottom>x.top-10:
                    "item is over"
                    if x.left<=item.left<=x.right or x.left<=item.right<=x.right:
                        "item is directly on top"
                        #print(hitListCount)
                        self.overtop[overtopCount] = 1
                        #print("set")
                    else:
                        self.overtop[overtopCount] = 0
                        #print("reverted")
                    
            
                if item.bottom == x.top and (x.left<=item.left<=x.right or x.left<=item.right<=x.right):
                    #print("works")
                    dy = 0
                else:
                    self.overtop[overtopCount] = 0
                    #print("reverted")            
            '''
            print("start", hitListCount)
            print(len(hitList[hitListCount]))
            print(self.overtop[overtopCount])
            print("end")
            print("\n")
            '''
            
            if len(hitList[hitListCount]) != 0 and self.overtop[overtopCount] > 0:
                dy = 0
                #print(self.overtop)
                
        
            
            if item.center_y <= 30:
                dy = 0
            
            item.center_y -= dy
            hitListCount += 1
            self.square_list.append(item)
            """
        if self.counter > counterTime * 15 and self.counter % 223 == 0:
            for item in self.square_list:
                item.kill()
                
                break
            """
            
        
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Animation")
    window.setup()
    arcade.run()
        
main()