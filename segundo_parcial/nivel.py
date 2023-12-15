import pygame
import time
import json
from pygame.locals import *
from jugador import *
from pinchos import *
from enemigo import *
from puerta import *
from llaves import *
from pantalla_pausa import *
from jefe_final import *

class Nivel():
    
    def __init__(self, indice_nivel, screen, globals):
        
        self.enemigos = []
        self.enemigos_disparo = []
        self.enemigos_disparo_2 = []
        self.disparos = []
        self.disparos_2 = []
        self.disparo_boss = []
        self.llaves = []
        self.llaves_obtenidas = 0
        self.game_over = 0
        self.pinchos = []
        self.lista_bloque = []
        self.indice_nivel = indice_nivel
        self.screen = screen
        self.jugador = None
        self.globals = globals
        self.fuente = pygame.font.Font(None, 36)
        if self.indice_nivel == 1:
            self.globals.puntaje = 0
            self.globals.cantidad_segundos = 0
        self.boss = None
        self.boss_vivo = True
        self.llave_boss = None
        self.image_corazon = pygame.image.load("Recursos\Imagenes/vida.png")
        self.image_corazon = pygame.transform.scale(self.image_corazon, (25,25))
        self.image_llaves = pygame.image.load("Recursos\Imagenes\llave_1.png")
        
    def instanciar_objetos(self):
        
        match self.indice_nivel:
            
            case 1:
                
                self.jugador = Jugador(100, self.globals.screen_alto - 210, self)
                
        
            case 2:
                
                self.jugador = Jugador(300, self.globals.screen_alto - 150, self)
            
            case 3:
                
                self.jugador = Jugador(300, self.globals.screen_alto - 150, self)
                
        
        
        with open("data/niveles.json","r") as archivo:
            
            lista_niveles = json.load(archivo)
            info = lista_niveles[(self.indice_nivel)-1]
    
        
        plat_bloque_1 = pygame.image.load("Recursos\Imagenes\piso_1.png")
        plat_bloque_2 = pygame.image.load("Recursos\Imagenes\piso_2.png")
        plat_bloque_3 = pygame.image.load("Recursos\Imagenes\piso_3.png")
        plat_bloque_4 = pygame.image.load("Recursos\Imagenes\piso_4.png")


        linea_cont = 0
        
        for linea in info:
            columna_cont = 0
            for bloque in linea:
                
                if bloque == 1:
                    imagen = pygame.transform.scale(plat_bloque_1, (self.globals.bloque_size, self.globals.bloque_size))
                    imagen_rect = imagen.get_rect()
                    imagen_rect.x = columna_cont * self.globals.bloque_size
                    imagen_rect.y = linea_cont * self.globals.bloque_size
                    bloque = (imagen, imagen_rect)
                    self.lista_bloque.append(bloque)
    
                if bloque == 2:
                    imagen = pygame.transform.scale(plat_bloque_2, (self.globals.bloque_size, self.globals.bloque_size))
                    imagen_rect = imagen.get_rect()
                    imagen_rect.x = columna_cont * self.globals.bloque_size
                    imagen_rect.y = linea_cont * self.globals.bloque_size
                    bloque = (imagen, imagen_rect)
                    self.lista_bloque.append(bloque)
                    
                if bloque == 3:
                    pincho = Pinchos(columna_cont * self.globals.bloque_size, linea_cont * self.globals.bloque_size, self.globals.bloque_size)
                    self.pinchos.append(pincho)
                    
                if bloque == 4:
                    enemigo = Enemigo(columna_cont * self.globals.bloque_size, linea_cont * self.globals.bloque_size, self.globals.bloque_size)
                    self.enemigos.append(enemigo)
                    
                if bloque == 5:
                    salida = Puerta_1(columna_cont * self.globals.bloque_size - 10, linea_cont * self.globals.bloque_size - 15, self.globals.bloque_size)
                    self.puerta = salida
                    
                if bloque == 6:
                    llaves = Llaves(columna_cont * self.globals.bloque_size + 10, linea_cont * self.globals.bloque_size)
                    self.llaves.append(llaves)   
                            
                if bloque == 7:
                    imagen = pygame.transform.scale(plat_bloque_3, (self.globals.bloque_size, self.globals.bloque_size))
                    imagen_rect = imagen.get_rect()
                    imagen_rect.x = columna_cont * self.globals.bloque_size
                    imagen_rect.y = linea_cont * self.globals.bloque_size
                    bloque = (imagen, imagen_rect)
                    self.lista_bloque.append(bloque)
                    
                if bloque == 8:
                    enemigo_dispara = Enemigo_dispara(columna_cont * self.globals.bloque_size, linea_cont * self.globals.bloque_size, self.globals.bloque_size)
                    self.enemigos_disparo.append(enemigo_dispara)
                    
                if bloque == 9:
                    salida = Puerta_2(columna_cont * self.globals.bloque_size - 10, linea_cont * self.globals.bloque_size - 15, self.globals.bloque_size)
                    self.puerta = salida   
                    
                if bloque == 10:
                    imagen = pygame.transform.scale(plat_bloque_4, (self.globals.bloque_size, self.globals.bloque_size))
                    imagen_rect = imagen.get_rect()
                    imagen_rect.x = columna_cont * self.globals.bloque_size
                    imagen_rect.y = linea_cont * self.globals.bloque_size
                    bloque = (imagen, imagen_rect)
                    self.lista_bloque.append(bloque)             
                
                if bloque == 11:
                    enemigo_dispara = Enemigo_dispara_2(columna_cont * self.globals.bloque_size, linea_cont * self.globals.bloque_size, self.globals.bloque_size)
                    self.enemigos_disparo_2.append(enemigo_dispara)
                       
                if bloque == 13:
                    self.boss = Boss_final(columna_cont * self.globals.bloque_size, linea_cont * self.globals.bloque_size + 10, self.globals.bloque_size)
                    self.llave_boss = Llaves(self.boss.rect.x, self.boss.rect.y)
                    self.llaves.append(self.llave_boss)
                
                columna_cont += 1
                
            linea_cont += 1

    def dibujar_bloque(self):
        for bloque in self.lista_bloque:
            self.screen.blit(bloque[0], bloque[1])
            
    def ejecutar_nivel(self):


        while True:
            
            
            minutos = self.globals.cantidad_segundos // 60
            segundos = self.globals.cantidad_segundos - (minutos * 60)
            texto_render = self.fuente.render(f"Puntaje: {self.globals.puntaje} | Tiempo: {minutos}:{segundos} | Vidas x{self.jugador.vidas} | Llaves Restantes x{len(self.llaves)}", True, (255,255,255))
            
            
            self.globals.clock.tick(60)
            self.screen.blit(self.globals.fondo, self.globals.origen)
            
            self.dibujar_bloque()

            # Iterar sobre la lista de enemigos y actualizar cada uno
            for enemigo in self.enemigos:
                enemigo.update()
                self.screen.blit(enemigo.image, enemigo.rect)
            
            
            for enemigo in self.enemigos_disparo:
                if enemigo.animar_disparo():
                    self.disparos.append(Disparo_enemigo(enemigo.rect.x, enemigo.rect.y, (20, 20)))
                self.screen.blit(enemigo.image, enemigo.rect)
                

            for enemigo in self.enemigos_disparo_2:
                enemigo.update()
                if enemigo.animar_disparo_2():
                    self.disparos_2.append(Disparo_enemigo_2(enemigo.rect.x, enemigo.rect.y, (20,20)))
                self.screen.blit(enemigo.image, enemigo.rect)

            self.puerta.actualizar_puerta()
            self.screen.blit(self.puerta.image, self.puerta.rect)
            
            if self.indice_nivel == 3 and self.boss.vida_boss > 0:
                
                if self.boss.update():
                    
                    self.disparo_boss.append(Disparo_boss(self.boss.rect.x, self.boss.rect.y))
                    
                self.llave_boss.rect.x = self.boss.rect.x + 40
                self.llave_boss.rect.y = self.boss.rect.y + 40
                    
                self.screen.blit(pygame.transform.flip(self.boss.image, self.boss.direccion_movimiento != -3, False), self.boss.rect) 
                
                
        
            # Iterar sobre la lista de pinchos y dibujar cada uno en pantalla
            for pincho in self.pinchos:
                self.screen.blit(pincho.image, pincho.rect)

            # Iterar sobre la lista de llaves y dibujar cada una en pantalla
            for llave in self.llaves:
                self.screen.blit(llave.image, llave.rect)

            self.game_over = self.jugador.actualizar(self.game_over, self.disparos, self.disparos_2, self.boss, self.disparo_boss)


            if self.indice_nivel == 3 and self.boss.vida_boss < 1 and self.boss_vivo:
                
                self.boss_vivo = False 
            
            
            
            if self.game_over == 1:
                time.sleep(1)
                
                if self.indice_nivel == 3:
                    
                    try:
                        with open("data\puntajes.json","r") as archivo:
                
                            info_lista_dics = json.load(archivo)
                    except:
                        print("Error al cargar el json")
                    
                    nuevo_jugador = {"puntaje": self.globals.puntaje, "tiempo": f"{minutos}:{segundos}"}
                
                    info_lista_dics.append(nuevo_jugador)
                    
                    with open("data\puntajes.json","w") as archivo:
                            
                        json.dump(info_lista_dics, archivo, indent=2)
                        
                
                
                return {"seguir": True, "accion": "gano"}
        
            elif self.game_over == 2:
                
                return {"seguir": True, "accion": "perdio"}
            

            if len(self.llaves) == 0:
                
                self.puerta.open = True
                self.puerta.actualizar_puerta()

            for evento in pygame.event.get():
                
                if evento.type == pygame.QUIT:

                    return {"seguir": False}
                
                if evento.type == self.globals.timer_segundos:
                    
                    self.globals.cantidad_segundos += 1   
                    
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    
                    # Obtener la posición del mouse al hacer clic
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    print(mouse_x, mouse_y)
                                        
                if evento.type == pygame.KEYDOWN: 
                    
                    if evento.key == pygame.K_ESCAPE:
                        
                        self.respuesta = Pantalla_pausa(self.globals).pausar()
                        
                        if not(self.respuesta["seguir"]):
                            
                            return{"seguir": False}
                        
                        else:
                            
                            if self.respuesta["accion"] == "atras":
                                
                                pass
                            
                            else:
                                
                                return self.respuesta
                            
                            
            

            
            pygame.draw.rect(self.screen, (0,0,0),(0,0,750,40))
            self.screen.blit(texto_render, (10, 10))
            # self.screen.blit(self.image_corazon, (31, 10))
            # self.screen.blit(self.image_llaves,(400, 10))
            pygame.display.flip()
