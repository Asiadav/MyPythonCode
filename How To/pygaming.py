import arcade
import random
import time

arcade.open_window(1920, 1080, "Drawing Example")
for i in range(1,100):
    arcade.set_background_color((random.randint(1,255),random.randint(1,255),random.randint(1,255)))

    arcade.start_render()

    arcade.draw_lrtb_rectangle_filled(random.randint(1,1000), random.randint(1001,1920), random.randint(1000,1920), random.randint(1,999), arcade.color.BITTER_LIME)

    arcade.draw_rectangle_filled(random.randint(1,1920), random.randint(1,1080), 450, 25,arcade.color.DARK_BLUE,random.randint(1,180))

    arcade.draw_point(random.randint(1,1920),random.randint(1,1080), arcade.color.RED, random.randint(1,100))

    arcade.draw_line(random.randint(1,1920), random.randint(1,1080), random.randint(1,1920), random.randint(1,1080), (random.randint(1,255),random.randint(1,255),random.randint(1,255)), 10)

    arcade.draw_circle_outline(random.randint(1,1920), random.randint(1,1080), 18, arcade.color.WISTERIA, 3)

    arcade.draw_text("AbSTracT aRT", random.randint(100,1820), random.randint(100,980), (random.randint(1,255),random.randint(1,255),random.randint(1,255)), random.randint(50,100),1)


    time.sleep(.1)
    arcade.finish_render()
    print(i)
arcade.run()




#arcade.close_window()
