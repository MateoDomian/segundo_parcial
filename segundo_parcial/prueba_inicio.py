import pygame
from pantalla_pausa import *



class Pantalla_inicio():
    
    def __init__(self, globals):
        
        self.fondo = pygame.image.load("Recursos\Imagenes/fondo_inicio.jpg")
        self.area1_rect = pygame.Rect(350, 260, 300, 110)
        self.area2_rect = pygame.Rect(350, 410, 300, 100)
        self.area3_rect = pygame.Rect(340, 560, 320, 100)
        self.area4_rect = pygame.Rect(350, 710, 300, 100)
        self.globals = globals
        

    
    def botones_inicio(self):
        
        while True:

            self.globals.screen.blit(self.fondo, self.globals.origen)
                
            for evento in pygame.event.get():
                
                if evento.type == pygame.QUIT:
                    
                    return {"seguir": False}

                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    
                    # Obtener la posición del mouse al hacer clic
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # Verificar si la posición del mouse está dentro de las áreas específicas
                    if self.area1_rect.collidepoint(mouse_x, mouse_y):
                        return {"seguir": True, "opcion": "jugar"}
                    elif self.area2_rect.collidepoint(mouse_x, mouse_y):
                        return {"seguir": True, "opcion": "puntuacion"}
                    elif self.area3_rect.collidepoint(mouse_x, mouse_y):
                        self.respuesta = Pantalla_pausa(self.globals).pausar()
                        
                        if not(self.respuesta["seguir"]):
                            
                            return{"seguir": False}

                    #falta implementar
                    elif self.area4_rect.collidepoint(mouse_x, mouse_y):
                        return {"seguir": False}

            pygame.display.flip()