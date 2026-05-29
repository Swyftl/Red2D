class physics:
    def __init__(self):
        self.objects = []

    def update(self):
        for obj in self.objects:
            obj.update()