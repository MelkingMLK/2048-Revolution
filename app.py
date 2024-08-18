import pygame
import sys
#######################################################################################
button_color = (137, 37, 238)
hover_color = (100, 160, 210)
text_color = (255, 255, 255)
title_color = (255, 85, 208)
log_color = (246, 248, 255)

copyright_color = (128, 128, 128)
STATE_MAIN_MENU = "main_menu"
STATE_REGISTER = "register"
STATE_Login = "login"
STATE_MODALITA_1 = "modalita_1"
STATE_MODALITA_2 = "modalita_2"
current_state = STATE_MAIN_MENU  
#######################################################################################
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1680, 1050))
pygame.display.set_caption("2048 Revolution")
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

def Main():
    background_image = pygame.image.load("./sf1.gif").convert()
    screen.blit(background_image, (0, 0))

    title_text = title_font.render("2048 Revolution", True, title_color)
    title_rect = title_text.get_rect()
    title_rect.topleft = (150, 150)
    screen.blit(title_text, title_rect)

    copyright_text = copyright_font.render("@Mlk Company 2024", True, copyright_color)
    copyright_rect = copyright_text.get_rect()
    copyright_rect.topleft = (0, 1030)
    screen.blit(copyright_text, copyright_rect)
    
    mouse_pos = pygame.mouse.get_pos()
    Button(button1, "Login", button1.collidepoint(mouse_pos))
    Button(button2, "Register", button2.collidepoint(mouse_pos))

def Register():
    StopMusic()
    background_image = pygame.image.load("./sf4.jpg").convert()
    screen.blit(background_image, (0, 0))
    title_text = title_font.render("Register ", True, log_color)
    title_rect = title_text.get_rect()
    title_rect.topleft = (650, 50)
    screen.blit(title_text, title_rect)

def Login():
    StopMusic()
    background_image = pygame.image.load("./sf4.jpg").convert()
    screen.blit(background_image, (0, 0))
    title_text = title_font.render("Login ", True, log_color)
    title_rect = title_text.get_rect()
    title_rect.topleft = (650, 50)
    screen.blit(title_text, title_rect)

#def Mod1():




def play_music(file, volume=0.15):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(volume)

def StopMusic():
    pygame.mixer.music.stop()

button1 = pygame.Rect(350, 350, 300, 60)
button2 = pygame.Rect(350, 450, 300, 60)
play_music("./jojo.mp3")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if current_state == STATE_MAIN_MENU:
                if button1.collidepoint(mouse_pos):
                    current_state = STATE_REGISTER
                elif button2.collidepoint(mouse_pos):
                    current_state = STATE_REGISTER
    if current_state == STATE_MAIN_MENU:
        Main()
    elif current_state == STATE_REGISTER:
        Register()
    elif current_state == STATE_MODALITA_1:
          Main() #Mod1()
    elif current_state == STATE_MODALITA_2:
          Main() #Mod2()

    pygame.display.flip()
