import pygame


class Boss_final(pygame.sprite.Sprite):
    def __init__(self, x, y, bloque_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.lista_boss = []
        
        for num in range(1,5):
            frame_boss = pygame.image.load(f"Recursos\Imagenes/boss_{num}.png")
            frame_boss = pygame.transform.scale(frame_boss, (90, 140))
            self.lista_boss.append(frame_boss)
        
        self.image = self.lista_boss[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.indice_foto = 0
        self.contador_loop = 0
        self.direccion_movimiento = -3
        self.vida_boss = 5
        self.init_x = x
        self.init_y = y
        
    def update(self):
    
        self.rect.x += self.direccion_movimiento
        self.contador_loop += 1
        if self.contador_loop > 260:
            self.direccion_movimiento *= -1
            
            self.contador_loop = 0  

        if self.contador_loop % 10 == 0:
            self.image = self.lista_boss[self.indice_foto]
            self.indice_foto += 1
        
            if self.indice_foto == 4:
                
                self.indice_foto = 0
        
        if self.contador_loop % 80 == 0:
            
            return True
        
        else:
            
            return False
        
    def reiniciar_variables(self):
            
        self.rect.x = self.init_x
        self.rect.y = self.init_y
        self.indice_foto = 0
        self.contador_loop = 0
        self.direccion_movimiento = -3
        
        self.image = self.lista_boss[0]
        
class Disparo_boss():
    
    def __init__(self, x, y,):
    
        self.image = pygame.image.load("Recursos\Imagenes\\bala_boss.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.gravedad = -15
        self.cooldown_reduccion_gravedad = 0
        