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
pygame.display.set_icon(icon)
window.blit(intro_img, (width // 2 - intro_img.get_width() // 2, height // 2 - intro_img.get_height() // 2))
pygame.display.update()
# pygame.mixer.Sound.play(intro_music)
# pygame.time.delay(5000)

running = True

while running:
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # pygame.display.update()
