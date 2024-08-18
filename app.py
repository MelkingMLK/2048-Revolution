import pygame
import sys
########################################################################################

button_color = (137, 37, 238)
hover_color = (100, 160, 210)
text_color = (255, 255, 255)
title_color = (255, 85, 208)
#copy_color= 
########################################################################################
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1680, 1050))
pygame.display.set_caption("2048 Revolution")
background_image = pygame.image.load("./sf1.gif").convert()
########################################################################################
font = pygame.font.Font(None, 40)
title_font = pygame.font.Font("./Font/DnaBeast-MDEv.ttf", 40) 
########################################################################################

def Button(rect, text, is_hovered):
    color = hover_color if is_hovered else button_color
    pygame.draw.rect(screen, color, rect)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)
 
def modalita_1():
    global background_image 
    pygame.mixer.music.stop()
    background_image = pygame.image.load("./sf2.jpg").convert() 


def modalita_2():
    print("Modalità 2 selezionata")

def draw_grid(rows, cols, cell_size, grid_color):
    # Calcola la dimensione della griglia
    grid_width = cols * cell_size
    grid_height = rows * cell_size
    
    # Calcola la posizione centrale della griglia
    start_x = (screen_width - grid_width) // 2
    start_y = (screen_height - grid_height) // 2
    
    # Disegna le linee orizzontali
    for row in range(rows + 1):
        pygame.draw.line(screen, grid_color, (start_x, start_y + row * cell_size), 
                         (start_x + grid_width, start_y + row * cell_size))
    
    # Disegna le linee verticali
    for col in range(cols + 1):
        pygame.draw.line(screen, grid_color, (start_x + col * cell_size, start_y), 
                         (start_x + col * cell_size, start_y + grid_height))
########################################################################################
pygame.mixer.music.load("./jojo.mp3")  
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.15)

title_text = title_font.render("2048 Revolution", True, title_color)
title_rect = title_text.get_rect()
title_rect.topleft = (150, 150)
button1 = pygame.Rect(350, 400, 300, 60)
button2= pygame.Rect(350, 500, 300, 60)
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
    mouse_pos = pygame.mouse.get_pos()
    Button(button1, "Login", button1.collidepoint(mouse_pos))
    Button(button2, "Register", button2.collidepoint(mouse_pos))
    pygame.display.flip()


    #adattabile, grafica, copyright