import arcade
window = arcade.open_window(500, 500, "Orbits")
window.set_update_rate(1/20)
window.set_mouse_visible(True)
window.on_mouse_motion(0, 0, 0, 0)
window.on_mouse_press(0, 0, 0, 0)
window.on_mouse_release(0, 0, 0, 0)
window.on_key_press(0, 0)
window.on_key_release(0, 0)
window.on_mouse_drag(0, 0, 1, 1, 1, 0)
window.on_mouse_scroll(1, 1, 1, 1)
window.on_draw()
window.on_resize(500, 500)
window.set_size(500, 500)
window.update(1/20)
window.set_visible(True)
#window.close()