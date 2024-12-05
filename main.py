import Red2D
import Red2D.Input

Engine = Red2D.Engine(1280, 720)

Character = Engine.new_player(0, 0, 10, 10)
block = Engine.new_Rectangle(20, 20, 10, 10)

move_left = Red2D.Input.Input("a")
move_right = Red2D.Input.Input("d")
move_up = Red2D.Input.Input("w")
move_down = Red2D.Input.Input("s")

TestText = Engine.new_Text("This is a test", 100, 100)

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
    TestText.text = str(Character.position)
    Engine.render_frame()
