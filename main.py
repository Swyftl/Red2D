import Red2D
import Red2D.Input
import Red2D.Player
Engine = Red2D.Engine(1280, 720)

Character = Red2D.Player.Player(Engine.Graphics, 10, 10, 10, 10)

move_left = Red2D.Input.Input("a")
move_right = Red2D.Input.Input("d")
move_up = Red2D.Input.Input("w")
move_down = Red2D.Input.Input("s")

while Engine.running:
    # Character Movement
    if move_up.is_pressed():
        Character.position.y -= 1
    elif move_down.is_pressed():
        Character.position.y += 1
    if move_left.is_pressed():
        Character.position.x -= 1
    elif move_right.is_pressed():
        Character.position.x += 1

    # Set the frame up with background
    Engine.tick("White")
    Engine.set_title("Frames Rendered: "+str(Engine.rendered_frames))
    # Render the player
    Character.render_player()
    # Finish up rendering and send the frame to the display
    Engine.render_frame()