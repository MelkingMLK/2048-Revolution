import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1680, 1050))
pygame.display.set_caption("2048 Revolution")
bck="./sf1.jpg"
background_image = pygame.image.load(bck).convert()

# Colori
button_color = (70, 130, 180)
hover_color = (100, 160, 210)
text_color = (255, 255, 255)

# Font
font = pygame.font.Font(None, 40)

# Definisci i bottoni
button1_rect = pygame.Rect(150, 400, 200, 60)
button2_rect = pygame.Rect(450, 400, 200, 60)

# Funzione per disegnare un bottone
def draw_button(rect, text, is_hovered):
    color = hover_color if is_hovered else button_color
    pygame.draw.rect(screen, color, rect)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

# Funzione per gestire la modalità 1
def modalita_1():
    print("Modalità 1 selezionata")

# Funzione per gestire la modalità 2
def modalita_2():
    print("Modalità 2 selezionata")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background_image, (0, 0))
    pygame.display.flip()
    # Disegna l'immagine di sfondo
    screen.blit(background_image, (0, 0))

    # Ottieni la posizione del mouse per l'effetto hover
    mouse_pos = pygame.mouse.get_pos()

    # Disegna i bottoni
    draw_button(button1_rect, "Modalità 1", button1_rect.collidepoint(mouse_pos))
    draw_button(button2_rect, "Modalità 2", button2_rect.collidepoint(mouse_pos))

    # Aggiorna il display
    pygame.display.flip()
