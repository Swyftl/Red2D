import Red2D
import Red2D.Input
import Red2D.Logging
import Red2D.config
import pygame

config = Red2D.config.config()

config.set("window_x", "1280")
config.set("window_y", "720")

config.set("framerate", "60")
config.set("background_color", "white")

Engine = Red2D.Engine(1280, 720)
Character = Engine.new_player(0, 0, 10, 10)

# Setting up the inputs
move_left = Red2D.Input.Input("a")
move_right = Red2D.Input.Input("d")
move_up = Red2D.Input.Input("w")
move_down = Red2D.Input.Input("s")

# Test Button
space = Red2D.Input.Input("space")

TestText = Engine.new_Text("[0, 0]", 0, 0)
framerate_display = Engine.new_Text(str(1/Engine.delta), 0, 50)

while Engine.running:
    # Character Movement
    if move_up.is_key_down():
        Character.position.y -= 100 * Engine.delta
    elif move_down.is_key_down():
        Character.position.y += 100 * Engine.delta
    if move_left.is_key_down():
        Character.position.x -= 100 * Engine.delta
    elif move_right.is_key_down():
        Character.position.x += 100 * Engine.delta

    if space.is_just_pressed():
        if TestText.visible:
            TestText.visible = False
        else:
            TestText.visible = True
    TestText.text = str(Character.position)
    framerate_display.text = str(str(1/Engine.delta))
    TestText.update()
    framerate_display.update()
    Engine.render_frame()