import Red2D

class Scene:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
    
    def remove_items(self, item):
        self.items.pop(item)

class Scene_Manager:

    def __init__(self, Engine):
        self.scenes = []
        self.Engine = Engine
    
    def new_scene(self):
        scene = Scene()
        self.scenes.append(scene)
        return scene
    
    def load_scene(self, scene):
        self.Engine.Render.shapes.clear_render()
        for item in scene:
            self.Engine.Render.shapes.add_shape(item)
    
    def clear_all_scenes(self):
        self.Engine.Render.shapes.clear_render()