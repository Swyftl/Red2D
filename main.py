import Red2D
import Red2D.Input
from Red2D.draw import Rectangle

Engine = Red2D.Engine(1280, 720)

Character = Engine.new_player(0, 0, 10, 10)
block = Rectangle(20, 20, 10, 10, Engine.Render, Engine.Graphics)

move_left = Red2D.Input.Input("a")
move_right = Red2D.Input.Input("d")
move_up = Red2D.Input.Input("w")
move_down = Red2D.Input.Input("s")

while Engine.running:
    # Character Movement
    if move_up.is_key_down():
        Character.position.y -= 1
    elif move_down.is_key_down():
        Character.position.y += 1
    if move_left.is_key_down():
        Character.position.x -= 1
    elif move_right.is_key_down():
        Character.position.x += 1

    # Set the frame up with background
    Engine.tick("White")
    # Render the player
    Engine.Render.render()
    if move_up.is_just_pressed():
        print("Just Pressed")
    # Finish up rendering and send the frame to the display
    Engine.render_frame()
