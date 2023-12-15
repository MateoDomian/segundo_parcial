import pygame
import time
import json
from pygame.locals import *


class Puerta_1(pygame.sprite.Sprite):
    def __init__(self, x, y, bloque_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Recursos\Imagenes\puerta_fin_cerrada.png")
        self.image = pygame.transform.scale(self.image, (bloque_size + 10, bloque_size + 15))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.open = False
        self.bloque_size = bloque_size
        
    def actualizar_puerta(self):
        
        if self.open:
            
            self.image = pygame.image.load("Recursos\Imagenes\puerta_fin_abierta.png")
            self.image = pygame.transform.scale(self.image, (self.bloque_size + 10, self.bloque_size + 15))
            self.rect = self.image.get_rect()
            self.rect.x = 890
            self.rect.y = 85
            
class Puerta_2(pygame.sprite.Sprite):
    
    def __init__(self, x, y, bloque_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Recursos\Imagenes\puerta_fin_cerrada_2.png")
        self.image = pygame.transform.scale(self.image, (bloque_size + 10, bloque_size + 15))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.open = False
        self.bloque_size = bloque_size
        
    def actualizar_puerta(self):
        
        if self.open:
            
            self.image = pygame.image.load("Recursos\Imagenes\puerta_fin_abierta_2.png")
            self.image = pygame.transform.scale(self.image, (self.bloque_size + 10, self.bloque_size + 15))
            self.rect = self.image.get_rect()
            self.rect.x = 890
            self.rect.y = 135