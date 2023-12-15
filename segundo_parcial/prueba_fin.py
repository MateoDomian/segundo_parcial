import pygame

pygame.init()

screen_ancho = 1000
screen_alto = 1000

screen = pygame.display.set_mode((screen_ancho, screen_alto))
fondo_inicio = pygame.image.load("./Recursos/Imagenes/fondo_fin.jpg")

origen = (0,0)

seguir = True

area1_rect = pygame.Rect(360, 300, 280, 100)
area2_rect = pygame.Rect(350, 450, 300, 100)
area3_rect = pygame.Rect(350, 600, 300, 100)
area4_rect = pygame.Rect(360, 740, 280, 100)

while seguir:

    screen.blit(fondo_inicio, origen)
        
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:

            seguir = False

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Obtener la posición del mouse al hacer clic
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if area1_rect.collidepoint(mouse_x, mouse_y):
                print("Clic en Área 1 (Botón 1)")
            elif area2_rect.collidepoint(mouse_x, mouse_y):
                print("Clic en Área 2 (Botón 2)")
            elif area3_rect.collidepoint(mouse_x, mouse_y):
                print("Clic en Área 3 (Botón 3)")
            elif area4_rect.collidepoint(mouse_x, mouse_y):
                print("Clic en Área 4 (Botón 4)")

    pygame.display.flip()