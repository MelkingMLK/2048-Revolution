import pygame
import sys
#######################################################################################
button_color = (137, 37, 238)
hover_color = (100, 160, 210)
text_color = (255, 255, 255)
title_color = (255, 85, 208)
copyright_color = (128, 128, 128)
#######################################################################################
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1680, 1050))
pygame.display.set_caption("2048 Revolution")
background_image = pygame.image.load("./sf1.gif").convert()
font = pygame.font.Font(None, 40)
title_font = pygame.font.Font("./Font/DnaBeast-MDEv.ttf", 40)
copyright_font = pygame.font.Font("./Font/PrStart.ttf", 10)
#######################################################################################

def Button(rect, text, is_hovered):
    color = hover_color if is_hovered else button_color
    pygame.draw.rect(screen, color, rect)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)
def Register()
    
def modalita_1():
    global background_image
    pygame.mixer.music.stop()
    background_image = pygame.image.load("./sf2.jpg").convert()

def modalita_2():
    print("Modalità 2 selezionata")
#######################################################################################
pygame.mixer.music.load("./jojo.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.15)

title_text = title_font.render("2048 Revolution", True, title_color)
title_rect = title_text.get_rect()
title_rect.topleft = (150, 150)
copyright_text = copyright_font.render("@Mlk Company 2024", True, copyright_color)
copyright_rect = copyright_text.get_rect()
copyright_rect.topleft = (0, 1030)  

button1 = pygame.Rect(350, 350, 300, 60)
button2 = pygame.Rect(350, 450, 300, 60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button1.collidepoint(mouse_pos):
                modalita_1()
            elif button2.collidepoint(mouse_pos):
                modalita_2()
    
    screen.blit(background_image, (0, 0))
    screen.blit(title_text, title_rect)
    screen.blit(copyright_text, copyright_rect)  # Draw the copyright text
    mouse_pos = pygame.mouse.get_pos()
    Button(button1, "Login", button1.collidepoint(mouse_pos))
    Button(button2, "Register", button2.collidepoint(mouse_pos))
    pygame.display.flip()
