import Red2D
import Red2D.Input

Engine = Red2D.Engine(1280, 720)

Character = Engine.new_player(0, 0, 10, 10)
block = Engine.new_Rectangle(20, 20, 10, 10)
test_sprite = Engine.new_Sprite(20, 20, 20, 20, (0, 0, 0))

newButton = Engine.new_Button(100, 100, 100, 50, "This is a test")
# Setting up the inputs
move_left = Red2D.Input.Input("a")
move_right = Red2D.Input.Input("d")
move_up = Red2D.Input.Input("w")
move_down = Red2D.Input.Input("s")

x_movement = Red2D.Input.Axis(move_left, move_right)
y_movement = Red2D.Input.Axis(move_up, move_down)

while Engine.running:
    # Character Movement
    Character.move(x_movement, y_movement)
    Engine.render_frame()
