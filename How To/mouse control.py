import arcade

# Set up the constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

RECT_WIDTH = 50
RECT_HEIGHT = 50


class Circle:
    """ Class to represent a circle on the screen """

    def __init__(self, x, y, size, color):
        """ Initialize our rectangle variables """

        # Position
        self.x = x
        self.y = y

        # Size and rotation
        self.size = size

        # Color
        self.color = color

    def draw(self):
        """ Draw cirrcle """
        arcade.draw_circle_filled(self.x, self.y, self.size,self.color)


class MyGame(arcade.Window):
    """ Main application class. """
    def __init__(self, width, height):
        super().__init__(width, height, title="Keyboard control")
        arcade.set_background_color((100,0,0))
        self.player = None
        self.left_down = False

    def setup(self):
        """ Set up the game and initialize the variables. """
        size = 10
        x = 0
        y = 0
        angle = 0
        color = arcade.color.WHITE

        self.player = Circle(x, y, size, color)
        self.left_down = False

    def update(self, dt):
        """ Move everything """
        if self.left_down:
            self.player.angle += 2

    def on_draw(self):
        """
        Render the screen.
        """
        self.player.draw()

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, buttons: int, modifiers: int):
        self.player.x = x
        self.player.y = y
    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.left_down = False


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.start_render()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()





'''
    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.player.x = x
        self.player.y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        print(button)
        if button == arcade.MOUSE_BUTTON_LEFT:
        self.left_down = True
'''

