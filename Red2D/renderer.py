class renderer:
    def __init__(self):
        self.objects = []

    def render(self):
        for obj in self.objects:
            obj.render()