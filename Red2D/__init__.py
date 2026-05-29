import pygame

class Engine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True

    def step(self):
        self.screen.fill((0, 0, 0))

        pygame.display.flip()
        self.clock.tick(60)

    def quit(self):
        self.running = False
        pygame.quit()