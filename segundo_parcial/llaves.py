import pygame


class Llaves(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Recursos\Imagenes\llave_1.png")
        self.image = pygame.transform.scale(self.image, (25, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.agarro = False