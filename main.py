import Red2D

Engine = Red2D.Engine(1280, 720)

while Engine.running:
    Engine.tick("White")
    Engine.set_title(Engine.rendered_frames)
    Engine.Graphics.render_rect("Red", Engine.Math.rect(10, 10, 10, 10))
    Engine.render_frame()