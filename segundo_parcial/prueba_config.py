import pygame

pygame.init()

screen_ancho = 1000
screen_alto = 1000

screen = pygame.display.set_mode((screen_ancho, screen_alto))
fondo_inicio = pygame.image.load("./Recursos/Imagenes/fondo_config.jpg")

origen = (0,0)

seguir = True

button_rect = pygame.Rect(360, 450, 280, 100)

while seguir:

    screen.blit(fondo_inicio, origen)
        
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:

            seguir = False

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Obtener la posición del mouse al hacer clic
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if button_rect.collidepoint(mouse_x, mouse_y):
                print("Clic en el botón")

    pygame.display.flip()