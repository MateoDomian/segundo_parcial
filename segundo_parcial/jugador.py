import pygame
import time
import json
from pygame.locals import *


class Jugador():
    def __init__(self, x, y, nivel):
        
        self.image_derecha = []
        self.image_izquierda = []
        self.images_idle = []
        self.images_jump = []
        self.images_muerte_derecha = []
        self.images_muerte_izquierda = []
        self.disparo_pantalla = []
        self.index = 0
        self.contador_animacion = 0
        self.open = False
        self.vidas = 3
        self.cordenadas = (x, y)
        self.nivel = nivel
        self.screen = self.nivel.screen
        self.globals = self.nivel.globals
        self.foto_game_over = pygame.image.load(f"Recursos\Imagenes/game_over.png")
        self.foto_game_over = pygame.transform.scale(self.foto_game_over, (400, 125))
        

        
        for num in range(1,6):
            frame_muerte_derecha = pygame.image.load(f"Recursos\Imagenes/muerte_{num}.png")
            frame_muerte_derecha = pygame.transform.scale(frame_muerte_derecha, (60, 60))
            self.images_muerte_derecha.append(frame_muerte_derecha)
            
            frame_muerte_izquierda = pygame.transform.flip(frame_muerte_derecha, True, False)
            self.images_muerte_izquierda.append(frame_muerte_izquierda)
        
        for num in range(1,5):
            
            if num > 2:
                frame_jump = pygame.image.load(f"Recursos\Imagenes/jump_{num-2}.png")
                frame_jump = pygame.transform.flip(frame_jump, True, False)
            else:
                frame_jump = pygame.image.load(f"Recursos\Imagenes/jump_{num}.png")
            frame_jump = pygame.transform.scale(frame_jump, (60, 60))
            self.images_jump.append(frame_jump)
            
        for num in range(1,5):
            
            frame_idle = pygame.image.load(f"Recursos\Imagenes/pj_idle_{num}.png")
            frame_idle = pygame.transform.scale(frame_idle, (60, 60))
            self.images_idle.append(frame_idle)
            
        for num in range(1,7):
            imagen_derecha = pygame.image.load(f"Recursos\Imagenes/run_{num}.png")
            imagen_derecha = pygame.transform.scale(imagen_derecha, (60, 60))
            imagen_izquierda = pygame.transform.flip(imagen_derecha, True, False)
            self.image_izquierda.append(imagen_izquierda)
            self.image_derecha.append(imagen_derecha)
            
        self.image = self.image_derecha[self.index]    
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.velocidad_y = 0
        self.salto = False
        self.direccion = 1
        self.cooldonw_caminar = 4
        self.cooldown_idle_1 = 40
        self.cooldown_idle_2 = 50
        self.cooldown_muerte = 7
        self.cooldown_frame_muerte = 0
        self.frame_actual_muerte = 0
        self.idle = True
        self.frame_idle = 0
        self.tiene_salto = True
        self.toca_piso = True

        
    def actualizar(self, game_over, lista_disparos, lista_disparos_2, boss, disparo_boss):
        
        velocidad_x = 0

        if game_over == 0:
            #teclas
            tecla = pygame.key.get_pressed()
            
            if tecla[pygame.K_SPACE] and self.salto == False and self.tiene_salto:
                if not self.toca_piso:
                    self.tiene_salto = False
                self.velocidad_y = -15
                self.salto = True
                
            if tecla[pygame.K_SPACE] == False:
                self.salto = False
            if tecla[pygame.K_LEFT]:
                velocidad_x -= 5
                self.contador_animacion += 1
                self.direccion = -1
            if tecla[pygame.K_RIGHT]:
                velocidad_x += 5    
                self.contador_animacion += 1
                self.direccion = 1
            if tecla[pygame.K_LEFT] == False and tecla[pygame.K_RIGHT] == False and tecla[pygame.K_SPACE] == False:
                self.counter = 0
                self.index = 0
                self.idle = True
                self.frame_idle += 1
                
                if self.direccion == 1:
                    if self.frame_idle < self.cooldown_idle_1:
                        self.image = self.images_idle[0]
                    elif self.frame_idle < self.cooldown_idle_2:
                        self.image = self.images_idle[1]
                    else:
                        self.frame_idle = 0
                        self.image = self.images_idle[0]
                        
                if self.direccion == -1:    
                    if self.frame_idle < self.cooldown_idle_1:
                        self.image = self.images_idle[2]
                    elif self.frame_idle < self.cooldown_idle_2:
                        self.image = self.images_idle[3]
                    else:
                        self.frame_idle = 0
                        self.image = self.images_idle[2]
                
                
            #animacion
            
            if self.contador_animacion > self.cooldonw_caminar:
                self.contador_animacion = 0        
                self.index += 1
                if self.index >= len(self.image_derecha):
                    self.index = 0
                if self.direccion == 1:
                    self.image = self.image_derecha[self.index]
                if self.direccion == -1:
                    self.image = self.image_izquierda[self.index] 
            if self.toca_piso == False:
                if self.direccion == 1:
                    if velocidad_x != 0:
                        self.image = self.images_jump[0]
                    else:
                        self.image = self.images_jump[1]
                if self.direccion == -1:          
                    if velocidad_x != 0:
                        self.image = self.images_jump[2] 
                    else:  
                        self.image = self.images_jump[3]
                    
            #gravedad y salto
            self.velocidad_y += 1
            if self.velocidad_y > 10:
                self.velocidad_y = 10
            
            #colisiones
            
            self.toca_piso = False
            
            for bloque in self.nivel.lista_bloque:
                # x
                if bloque[1].colliderect(self.rect.x + velocidad_x, self.rect.y, self.width, self.height):
                
                    velocidad_x = 0
                
                # y
                if bloque[1].colliderect(self.rect.x, self.rect.y + self.velocidad_y, self.width, self.height):
                    # choca arriba
                    if self.velocidad_y < 0:
                        self.rect.top = bloque[1].bottom
                        self.velocidad_y = 0
                    # choca abajo
                    elif self.velocidad_y >= 0:

                        self.rect.bottom = bloque[1].top
                        self.velocidad_y = 0
                        self.tiene_salto = True
                        self.toca_piso = True
                        
            #colisiones pinchos
            
            if pygame.sprite.spritecollide(self, self.nivel.pinchos, False):
                
                self.vidas -= 1
                self.globals.sonido_muerte.play()   
                
                if self.vidas < 1:
                    
                    game_over = -1
                    self.globals.sonido_gameover.play() 
                    
                else:
                    self.rect.x = self.cordenadas[0]
                    self.rect.y = self.cordenadas[1]
                    time.sleep(2)
                    
            #colisiones enemigo
            

                    
            i = 0
            
            enemigos_borrar = []

            for enemigo in self.nivel.enemigos:
                
                self.rect.colliderect(enemigo.rect)
                
                if self.rect.colliderect(enemigo.rect):

                    if self.velocidad_y > 0:
                    
                        enemigos_borrar.append(i)
                        self.velocidad_y = -10
                        self.globals.puntaje += 50
                        
                    else:
                        
                        self.vidas -= 1
                        self.globals.sonido_muerte.play() 
                        
                        if self.vidas < 1:
                            game_over = -1
                            self.globals.sonido_gameover.play() 
                            
                        else:
                            time.sleep(1)
                            self.rect.x = self.cordenadas[0]
                            self.rect.y = self.cordenadas[1]    
                i += 1
                
            if len(enemigos_borrar) != 0:
                
                self.nivel.enemigos.pop(enemigos_borrar[0])
            
            
            disparos_restantes = []
            
            for disparo in lista_disparos:
                
                disparo.rect.x -= 6
                
                self.screen.blit(disparo.image, disparo.rect)
                
                if not(self.rect.colliderect(disparo.rect) or disparo.rect.x < 0):
                    
                    disparos_restantes.append(disparo)
                
                if self.rect.colliderect(disparo.rect):
                        
                    self.vidas -= 1
                    self.globals.sonido_muerte.play() 
                    if self.vidas < 1:
                        game_over = -1
                        self.globals.sonido_gameover.play() 
                        
                    else:
                        time.sleep(1)
                        self.rect.x = self.cordenadas[0]
                        self.rect.y = self.cordenadas[1]
            
            self.nivel.disparos = disparos_restantes  
                        
                    
                    
            disparos_2_restantes = []
            
            for disparo in lista_disparos_2:
                
                disparo.rect.y += 5
                
                self.screen.blit(disparo.image, disparo.rect)
                
                if not(self.rect.colliderect(disparo.rect) or disparo.rect.y > self.globals.screen_alto):
                        
                    disparos_2_restantes.append(disparo)
                    
                if self.rect.colliderect(disparo.rect):
                    
                    self.vidas -= 1
                    self.globals.sonido_muerte.play() 
                    
                    if self.vidas < 1:
                        game_over = -1
                        self.globals.sonido_gameover.play() 
                        
                    else:
                        time.sleep(1)
                        self.rect.x = self.cordenadas[0]
                        self.rect.y = self.cordenadas[1]  
            
            self.nivel.disparos_2 = disparos_2_restantes
                
    
            
            if self.nivel.indice_nivel == 3:
                
                if self.rect.colliderect(boss.rect) and self.nivel.boss_vivo:
                    
                    if self.velocidad_y > 0:
                        
                            self.velocidad_y = -25
                            self.globals.puntaje += 50
                            boss.vida_boss -= 1

                    else:
                        
                        self.vidas -= 1
                        self.globals.sonido_muerte.play() 
                        boss.reiniciar_variables()
                        
                        if self.vidas < 1:
                            game_over = -1
                            self.globals.sonido_gameover.play() 
                            
                        else:
                            time.sleep(1)
                            self.rect.x = self.cordenadas[0]
                            self.rect.y = self.cordenadas[1]    
                
                
                disparos_piedra = []
                    
                for piedra in disparo_boss:
                    
                    piedra.cooldown_reduccion_gravedad += 1
                    
                    if piedra.cooldown_reduccion_gravedad == 6:
                        
                        piedra.gravedad += 1
                        piedra.cooldown_reduccion_gravedad = 0
                    
                    piedra.rect.y += piedra.gravedad
                
                    self.screen.blit(piedra.image, piedra.rect)
                
                
                    if not(self.rect.colliderect(piedra.rect) or piedra.rect.y > self.globals.screen_alto):
                            
                        disparos_piedra.append(piedra)
                    
                    if self.rect.colliderect(piedra.rect):
                        
                        self.vidas -= 1
                        self.globals.sonido_muerte.play() 
                        boss.reiniciar_variables()
                    
                        if self.vidas < 1:
                            game_over = -1
                            self.globals.sonido_gameover.play() 
                            
                        else:
                            time.sleep(1)
                            self.rect.x = self.cordenadas[0]
                            self.rect.y = self.cordenadas[1]  
                        
                self.nivel.disparo_boss = disparos_piedra
                                        
            
            
            
            
         

            borrar = False
            indice = 0
        
            for i in list(range(0,len(self.nivel.llaves))):
                
                if self.nivel.llaves[i].rect.colliderect(self.rect):
                    
                    self.globals.sonido_llave.play()
                    self.globals.puntaje += 10
                    borrar = True
                    indice = i
                        
            if borrar != False:
                
                self.nivel.llaves.pop(indice)
                
                if len(self.nivel.llaves) == 0:
                    
                    self.globals.puntaje += 100
            
            #colisiones puerta     
            
            if len(self.nivel.llaves) == 0:
                
                if self.rect.colliderect(self.nivel.puerta.rect):
                    game_over = 1
                        
                
            #actualizar coordenadas
            self.rect.x += velocidad_x
            self.rect.y += self.velocidad_y
            
            #animacion de muerte
        elif game_over == -1:
            
            self.cooldown_frame_muerte += 1
            
            if self.cooldown_frame_muerte == self.cooldown_muerte and self.frame_actual_muerte < 4:
                self.frame_actual_muerte += 1
                self.cooldown_frame_muerte = 0
                
            if self.direccion == 1:
                self.image = self.images_muerte_derecha[self.frame_actual_muerte]
                
            else:
                self.image = self.images_muerte_izquierda[self.frame_actual_muerte]
            
            self.screen.blit(self.foto_game_over, (325, 410))

            if self.cooldown_frame_muerte > 100:
                
                return 2
            
            
        #blitear pj
        self.screen.blit(self.image, self.rect)
        
        return game_over 
    