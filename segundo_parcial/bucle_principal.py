import pygame
import time
import json
from nivel import *
from pygame.locals import *
from prueba_inicio import *
from tablero import *
from tablero import Tablero


class Bucle_principal():
    
    def __init__(self):
        
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.screen_ancho = 1000
        self.screen_alto = 1000
        self.screen = pygame.display.set_mode((self.screen_ancho, self.screen_alto))
        self.fondo = pygame.image.load('Recursos\Imagenes/fondo.png')
        self.origen = (0, 0)
        self.bloque_size = 50
        self.game_over = 0
        self.pantalla_actual = "inicio"
        self.indice_nivel = 1
        self.seguir = True
        self.respuesta = None
        self.timer_segundos = pygame.USEREVENT+1
        pygame.time.set_timer(self.timer_segundos, 1000)
        self.puntaje = 0
        self.cantidad_segundos = 0
        self.musica_on = True
        self.volumen = 1
        self.musica_fondo = "Recursos\sonidos\sonido_musica.wav"
        
        self.sonido_llave = pygame.mixer.Sound("Recursos\sonidos\sonido_llave.wav")
        self.sonido_gameover = pygame.mixer.Sound("Recursos\sonidos\sonido_gameover.wav")
        self.sonido_puerta = pygame.mixer.Sound("Recursos\sonidos\sonido_puerta.wav")
        self.sonido_muerte = pygame.mixer.Sound("Recursos\sonidos\sonido_muerte.wav")
        
    def actualizar_volumen(self):
        
        pygame.mixer.music.set_volume(self.volumen)
        self.sonido_llave.set_volume(self.volumen)
        self.sonido_gameover.set_volume(self.volumen)
        self.sonido_puerta.set_volume(self.volumen)
        self.sonido_muerte.set_volume(self.volumen)

        
    def comenzar_juego(self):    
            
        
        
        pygame.mixer.music.load(self.musica_fondo)
        pygame.mixer.music.play(-1)

        pygame.display.set_caption('Mike warrior')
        
        while self.seguir:
            
            if self.pantalla_actual == "inicio":
                
                respuesta = Pantalla_inicio(self).botones_inicio()
                
                if respuesta["seguir"]: 
                    
                    if respuesta["opcion"] == "jugar":
                        
                        self.pantalla_actual = "nivel"
                    
                    if respuesta["opcion"] == "puntuacion":
                        
                        self.pantalla_actual = "puntuacion"

                else:
                    
                    self.seguir = False
            
            if self.pantalla_actual == "puntuacion":
                
                respuesta = Tablero(self).mostrar_puntaje()
                
                if respuesta["seguir"]:
                    
                    self.pantalla_actual = "inicio"
                    self.indice_nivel = 1
                
                else:
                    
                    self.seguir = False    
                
            
            if self.pantalla_actual == "nivel":
                
                self.nivel = Nivel(self.indice_nivel, self.screen, self)
                self.nivel.instanciar_objetos()
                self.respuesta = self.nivel.ejecutar_nivel()
                
                if self.respuesta["seguir"]:
                    
                    if self.respuesta["accion"] == "gano":
                        
                        self.indice_nivel += 1
                        
                        if self.indice_nivel == 4:
                            
                            self.pantalla_actual = "puntuacion"
                        
                    else:
                        
                        self.pantalla_actual = "inicio"
                        self.indice_nivel = 1
                    
                else: 
                    
                    self.seguir = False
                    
                
            
                
        pygame.quit()


