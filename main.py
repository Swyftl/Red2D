import Red2D
import Red2D.Input
import Red2D.Logging

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

# Test Button
space = Red2D.Input.Input("space")

TestText = Engine.new_Text("[0, 0]", 100, 100)

Engine.Logging.log("This is a test", level="Log")
Engine.Logging.log("This is a test", level="Error")
Engine.Logging.log("This is a test", level="Critical")

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
    TestText.update()
    Engine.render_frame()
