import os
import time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame 
pygame.init()

width = 1200
height = 700

window = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Kaun Banega Crorepati")
icon = pygame.image.load("images/logo.png")
intro_img = pygame.image.load("images/intro.jpeg")
intro_music = pygame.mixer.Sound("audio/intro.ogg")
start_music = pygame.mixer.Sound("audio/start.ogg")
play_img = pygame.image.load("images/play.png")
quit_img = pygame.image.load("images/quit.png")
pygame.display.set_icon(icon)

window.blit(intro_img, (width // 2 - intro_img.get_width() // 2, height // 2 - intro_img.get_height() // 2))
pygame.display.update()
pygame.mixer.Sound.play(intro_music)
pygame.time.delay(5000)

quit_img_loc = (play_img.get_width(), 500)
play_img_loc = (0, 500)

running = True

def is_over(pos, up, down, trim):
    up = (up[0]+trim, up[1])
    down = (down[0]-trim, down[1])
    if pos[0] > up[0] and pos[1] > up[1]:
        if pos[0] < up[0] + down[0] and pos[1] < up[1] + down[1]:
            return True
    else:
        return False
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.Font('fonts/RobotoSlab-Medium.ttf', 80)
play_txt = font.render('Play', True, white)
quit_txt = font.render('Quit', True, white)
play_txt_rect = play_txt.get_rect()
quit_txt_rect = quit_txt.get_rect()
play_txt_rect.center = (300, 560)
quit_txt_rect.center = (900, 560)

def start_window():
    running = True
    while running:
        window.blit(quit_img, quit_img_loc)
        window.blit(play_img, play_img_loc)
        window.blit(play_txt, play_txt_rect)
        window.blit(quit_txt, quit_txt_rect)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if is_over(pos, play_img_loc, play_img.get_size(), 60):
                    pygame.mixer.Sound.play(start_music)
                    print("Start")

                if is_over(pos, quit_img_loc, quit_img.get_size(), 60):
                    running = False

        pygame.display.update()


start_window()