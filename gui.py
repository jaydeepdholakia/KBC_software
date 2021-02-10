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
quit_img_over = pygame.image.load("images/quit_over.png")
play_img_over = pygame.image.load("images/quit_over.png")
game_bg_img = pygame.image.load("images/bg.png")
question_img = pygame.image.load("images/question.png")

opt_a_img = pygame.image.load("images/opt_l.png")
opt_b_img = pygame.image.load("images/opt_r.png")
opt_c_img = pygame.image.load("images/opt_l.png")
opt_d_img = pygame.image.load("images/opt_r.png")

pygame.display.set_icon(icon)

# window.blit(intro_img, (0, 0))
# pygame.display.update()
# pygame.mixer.Sound.play(intro_music)
# pygame.time.delay(5000)

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
gold = (218,165,32)
intro_font = pygame.font.Font('fonts/RobotoSlab-Medium.ttf', 80)
question_font = pygame.font.Font('fonts/RobotoSlab-Medium.ttf', 30)
opt_char_font = pygame.font.Font('fonts/RobotoSlab-SemiBold.ttf', 40)
opt_font = pygame.font.Font('fonts/RobotoSlab-Medium.ttf', 35)
play_txt = intro_font.render('Play', True, white)
quit_txt = intro_font.render('Quit', True, white)
play_txt_rect = play_txt.get_rect()
quit_txt_rect = quit_txt.get_rect()
play_txt_rect.center = (300, 560)
quit_txt_rect.center = (900, 560)

def game_window():
    global question_font
    global opt_char_font
    global opt_font

    opt_a_char_txt = opt_char_font.render("A:", True, gold)
    opt_b_char_txt = opt_char_font.render("B:", True, gold)
    opt_c_char_txt = opt_char_font.render("C:", True, gold)
    opt_d_char_txt = opt_char_font.render("D:", True, gold)

    opt_a_char_txt_rect = opt_a_char_txt.get_rect()
    opt_b_char_txt_rect = opt_b_char_txt.get_rect()
    opt_c_char_txt_rect = opt_c_char_txt.get_rect()
    opt_d_char_txt_rect = opt_d_char_txt.get_rect()

    opt_a_char_txt_rect.center = (120, 435)
    opt_b_char_txt_rect.center = (680, 435)
    opt_c_char_txt_rect.center = (120, 540)
    opt_d_char_txt_rect.center = (680, 540)

    question_txt = question_font.render('Yeah its not necessary if you have two nested loop then the time ', True, white)
    opt_a_txt = opt_font.render('Opthion A', True, white)
    opt_b_txt = opt_font.render('Opthion B', True, white)
    opt_c_txt = opt_font.render('Opthion C', True, white)
    opt_d_txt = opt_font.render('Opthion D', True, white)

    question_txt_rect = question_txt.get_rect()
    opt_a_txt_rect = opt_a_txt.get_rect()
    opt_b_txt_rect = opt_b_txt.get_rect()
    opt_c_txt_rect = opt_c_txt.get_rect()
    opt_d_txt_rect = opt_d_txt.get_rect()

    question_txt_rect.center = (610, 250)
    opt_a_txt_rect.center = (235, 435)
    opt_b_txt_rect.center = (790, 435)
    opt_c_txt_rect.center = (235, 540)
    opt_d_txt_rect.center = (790, 540)


    # pygame.mixer.Sound.play(start_music)
    running = True
    while running:
        window.blit(game_bg_img, (0, 0))
        window.blit(question_img, (0, 200))
        window.blit(opt_a_img, (0, 400))
        window.blit(opt_b_img, (600, 400))
        window.blit(opt_c_img, (0, 500))
        window.blit(opt_d_img, (600, 500))

        window.blit(question_txt, question_txt_rect)
        window.blit(opt_a_txt, opt_a_txt_rect)
        window.blit(opt_b_txt, opt_b_txt_rect)
        window.blit(opt_c_txt, opt_c_txt_rect)
        window.blit(opt_d_txt, opt_d_txt_rect)

        window.blit(opt_a_char_txt, opt_a_char_txt_rect)
        window.blit(opt_b_char_txt, opt_b_char_txt_rect)
        window.blit(opt_c_char_txt, opt_c_char_txt_rect)
        window.blit(opt_d_char_txt, opt_d_char_txt_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        pygame.display.update()


def start_window():
    pos = (0, 0)
    while True:
        window.blit(quit_img, quit_img_loc)
        window.blit(play_img, play_img_loc)

        if is_over(pos, quit_img_loc, quit_img.get_size(), 60):
            window.blit(quit_img_over, quit_img_loc)
        
        if is_over(pos, play_img_loc, play_img.get_size(), 60):
            window.blit(play_img_over, play_img_loc)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if is_over(pos, play_img_loc, play_img.get_size(), 60):
                    print("Start")
                    game_window()
                    return 0

                if is_over(pos, quit_img_loc, quit_img.get_size(), 60):
                    return 0

        window.blit(play_txt, play_txt_rect)
        window.blit(quit_txt, quit_txt_rect)

        pygame.display.update()


game_window()