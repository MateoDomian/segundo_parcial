import pygame


class Pantalla_pausa():
    
    def __init__(self, globals):
        
        self.imagen_fondo = pygame.image.load("Recursos\Imagenes\pantalla_config.png")
        self.globals = globals
        self.screen = self.globals.screen
        
        self.area1_rect = pygame.Rect(360, 385, 280, 100)
        self.area2_rect = pygame.Rect(350, 590, 300, 100)
        self.area3_rect = pygame.Rect(360, 690, 270, 95)
        self.sonido_musica = pygame.Rect(350, 240, 60, 60)
        self.sonido_volumen = pygame.Rect(540, 240, 60, 60)
        
        self.imagen_music_on = pygame.image.load("Recursos\Imagenes/boton_musica_on.png")
        self.imagen_music_off = pygame.image.load("Recursos\Imagenes/boton_musica_off.png")
        self.imagen_vol_alto = pygame.image.load("Recursos\Imagenes/boton_volumen_alto.png")
        self.imagen_vol_medio = pygame.image.load("Recursos\Imagenes/boton_volumen_medio.png")
        self.imagen_vol_off =  pygame.image.load("Recursos\Imagenes/boton_volumen_off.png")

        
    def pausar(self):
        
        while True:
            
            self.screen.blit(self.imagen_fondo, (0,0))
            
            
            if self.globals.musica_on:
                
                self.screen.blit(self.imagen_music_on, self.sonido_musica)
            
            else: 
                
                self.screen.blit(self.imagen_music_off, self.sonido_musica)
                
            if self.globals.volumen == 1:
                
                self.screen.blit(self.imagen_vol_alto, self.sonido_volumen)
            
            elif self.globals.volumen == 0.5:
                
                self.screen.blit(self.imagen_vol_medio, self.sonido_volumen)
                
            elif self.globals.volumen == 0:
                
                self.screen.blit(self.imagen_vol_off, self.sonido_volumen)
            
            
            for evento in pygame.event.get():
                
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    
                    if self.area1_rect.collidepoint(mouse_x, mouse_y):
                        
                        return {"seguir": True, "accion": "atras"}
                    
                    elif self.area2_rect.collidepoint(mouse_x, mouse_y):
                        
                        return {"seguir": True, "accion": "menu"}
                    
                    elif self.area3_rect.collidepoint(mouse_x, mouse_y):
                        
                        return {"seguir": False}
                    
                    elif self.sonido_musica.collidepoint(mouse_x,mouse_y):
                        
                        if self.globals.musica_on:
                            
                            pygame.mixer.music.pause()
                            self.globals.musica_on = False
                            
                        else:
                                                        
                            pygame.mixer.music.unpause()
                            self.globals.musica_on = True
                            
                    
                    elif self.sonido_volumen.collidepoint(mouse_x, mouse_y):
                        
                        if self.globals.volumen == 1:
                            
                            self.globals.volumen = 0
                        
                        elif self.globals.volumen == 0.5:
                            
                            self.globals.volumen = 1
                            
                        elif self.globals.volumen == 0:
                            
                            self.globals.volumen = 0.5
                    
                        self.globals.actualizar_volumen()
                        
                if evento.type == pygame.KEYDOWN: 
                    
                    if evento.key == pygame.K_ESCAPE:

                        return {"seguir": True, "accion": "atras"}

                if evento.type == pygame.QUIT:

                    return {"seguir": False}
                
            pygame.display.flip()        
                