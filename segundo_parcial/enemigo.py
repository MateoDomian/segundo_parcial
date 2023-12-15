import pygame
import time
import json
from pygame.locals import *


class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, bloque_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Recursos\Imagenes\enemigo_1.png")
        self.image = pygame.transform.scale(self.image, (bloque_size, bloque_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direccion_movimiento = 1
        self.contador_direccion = 0
        
    def update(self):
        
        self.rect.x += self.direccion_movimiento
        self.contador_direccion += 1
        if self.contador_direccion > 100:
            self.direccion_movimiento *= -1
            self.image = pygame.transform.flip(self.image, True, False)
            self.contador_direccion = -40
        
        
class Enemigo_dispara(pygame.sprite.Sprite):
    
    def __init__(self, x, y, bloque_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.images_disparo = []
        
        for num in range(1,4):
            frame_disparo_enemigo = pygame.image.load(f"Recursos\Imagenes\enemigo_dispara_{num}.png")
            frame_disparo_enemigo = pygame.transform.scale(frame_disparo_enemigo, (bloque_size, bloque_size))
            self.images_disparo.append(frame_disparo_enemigo)
        
        self.image = self.images_disparo[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.index = 0
        self.contador = 0
        self.cooldown = 0
        
        

    def animar_disparo(self):
        
        self.contador += 1
        if self.contador > 100:
            self.cooldown += 1
            if self.cooldown >= 7:
                self.index += 1
                self.cooldown = 0
            if self.disparar():
                return True
        else:
            self.image = self.images_disparo[self.index]
        
        
    def disparar(self):
        
        if self.index < len(self.images_disparo):
            self.image = self.images_disparo[self.index]
            self.image = self.images_disparo[self.index]
            if self.index >= len(self.images_disparo)-1:
                self.index = 0
                self.contador = 0
                return True
        else:
            self.index = 0
            self.contador = 0

    
class Disparo_enemigo():
    
    def __init__(self, x, y, bloque_size):
        
        self.image = pygame.image.load("Recursos\Imagenes\disparo_enemigo_1.png")
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    
class Enemigo_dispara_2(pygame.sprite.Sprite):
    
    def __init__(self, x, y, bloque_size):
        pygame.sprite.Sprite.__init__(self)
        self.enemigo_volador = []
        
        for num in range(1,4):
            frame_disparo_enemigo = pygame.image.load(f"Recursos\Imagenes\enemigo_volador_{num}.png")
            frame_disparo_enemigo = pygame.transform.scale(frame_disparo_enemigo, (bloque_size, bloque_size))
            self.enemigo_volador.append(frame_disparo_enemigo)
        
        self.image = self.enemigo_volador[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.index = 0
        self.contador = 0
        self.cooldown = 0
        self.direccion_movimiento = 1
        self.contador_direccion = 0
        
    def update(self):
    
        self.rect.x += self.direccion_movimiento
        self.contador_direccion += 1
        if self.contador_direccion > 200:
            self.direccion_movimiento *= -1
            self.image = pygame.transform.flip(self.image, True, False)
            self.contador_direccion = -100
    
    def animar_disparo_2(self):
        
        self.contador += 1
        if self.contador > 100:
            self.cooldown += 1
            if self.cooldown >= 5:
                self.index += 1
                self.cooldown = 0
            if self.disparar_2():
                return True
        else:
            self.image = pygame.transform.flip(self.enemigo_volador[self.index], self.direccion_movimiento != 1, False)
        
        
    def disparar_2(self):
        
        if self.index < len(self.enemigo_volador):
            self.image = pygame.transform.flip(self.enemigo_volador[self.index], self.direccion_movimiento != 1, False)
            if self.index >= len(self.enemigo_volador)-1:
                self.index = 0
                self.contador = 0
                return True
        else:
            self.index = 0
            self.contador = 0
            
            
class Disparo_enemigo_2():
    
    def __init__(self, x, y, bloque_size):
        
        self.image = pygame.image.load("Recursos\Imagenes\disparo_enemigo_2.png")
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y