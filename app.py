import pygame
import sys
########################################################################################
bck="./sf1.gif"
button_color = (137, 37, 238)
hover_color = (100, 160, 210)
text_color = (255, 255, 255)
title_color = (255, 85, 208)
########################################################################################
pygame.init()
screen = pygame.display.set_mode((1680, 1050))
pygame.display.set_caption("2048 Revolution")
background_image = pygame.image.load(bck).convert()
########################################################################################
font = pygame.font.Font(None, 40)
title_font = pygame.font.Font(None, 60) 
########################################################################################
# Funzione per disegnare un bottone
def Button(rect, text, is_hovered):
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
########################################################################################
title_text = title_font.render("2048 Revolution", True, title_color)
title_rect = title_text.get_rect()
title_rect.topleft = (200, 300)
button1 = pygame.Rect(200, 400, 200, 60)
button2= pygame.Rect(200, 500, 200, 60)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button1.collidepoint(mouse_pos):
                modalita_1()
            elif button.collidepoint(mouse_pos):
                modalita_2()
    screen.blit(background_image, (0, 0))
    screen.blit(title_text, title_rect)
    mouse_pos = pygame.mouse.get_pos()
    Button(button1, "Modalità 1", button1.collidepoint(mouse_pos))
    Button(button2, "Modalità 2", button2.collidepoint(mouse_pos))
    pygame.display.flip()