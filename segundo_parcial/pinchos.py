import pygame
import time
import json
from pygame.locals import *

class Pinchos(pygame.sprite.Sprite):
    def __init__(self, x, y, bloque_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Recursos\Imagenes\pincho.png")
        self.image = pygame.transform.scale(self.image, (bloque_size, bloque_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y