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
lock_music = pygame.mixer.Sound("audio/lock.ogg")
wrong_music = pygame.mixer.Sound("audio/wrong.ogg")

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


opt_a_img_over = pygame.image.load("images/opt_l_over.png")
opt_b_img_over = pygame.image.load("images/opt_r_over.png")
opt_c_img_over = pygame.image.load("images/opt_l_over.png")
opt_d_img_over = pygame.image.load("images/opt_r_over.png")

opt_a_img_lock = pygame.image.load("images/opt_l_lock.png")
opt_b_img_lock = pygame.image.load("images/opt_r_lock.png")
opt_c_img_lock = pygame.image.load("images/opt_l_lock.png")
opt_d_img_lock = pygame.image.load("images/opt_r_lock.png")

opt_a_img_wrong = pygame.image.load("images/opt_l_wrong.png")
opt_b_img_wrong = pygame.image.load("images/opt_r_wrong.png")
opt_c_img_wrong = pygame.image.load("images/opt_l_wrong.png")
opt_d_img_wrong = pygame.image.load("images/opt_r_wrong.png")

opt_a_img_correct = pygame.image.load("images/opt_l_correct.png")
opt_b_img_correct = pygame.image.load("images/opt_r_correct.png")
opt_c_img_correct = pygame.image.load("images/opt_l_correct.png")
opt_d_img_correct = pygame.image.load("images/opt_r_correct.png")

pygame.display.set_icon(icon) 

window.blit(intro_img, (0, 0)) 
pygame.display.update() 
pygame.mixer.Sound.play(intro_music) 
pygame.time.delay(5000) 

quit_img_loc = (play_img.get_width(), 500) 
play_img_loc = (0, 500) 

opt_a_img_loc = (0, 400) 
opt_b_img_loc = (600, 400) 
opt_c_img_loc = (0, 500) 
opt_d_img_loc = (600, 500) 

running = True

def is_over(pos, up, down, trim): 
    up = (up[0]+trim, up[1]) 
    down = (down[0]-trim, down[1]) 
    if pos[0] > up[0] and pos[1] > up[1]: 
        if pos[0] < up[0] + down[0] and pos[1] <  up[1] + down[1]:
            return True 
    else:
        return False 

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
gold = (218,165,32) 
black = (0, 0, 0)
grey = (90, 90, 90) 
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

question = 'Yeah its not necessary if you have two nested loop then the time '
opt_a = "Option A" 
opt_b = "Option B" 
opt_c = "Option C" 
opt_d = "Option D" 

question_txt = question_font.render(question, True, white)
opt_a_txt = opt_font.render(opt_a, True, white) 
opt_b_txt = opt_font.render(opt_b, True, white) 
opt_c_txt = opt_font.render(opt_c, True, white) 
opt_d_txt = opt_font.render(opt_d, True, white) 

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


lock_data = {
    "a": [opt_a, opt_a_img_lock, opt_a_img_wrong, opt_a_img_correct, opt_a_img_loc, opt_a_txt_rect, opt_a_char_txt_rect],
    "b": [opt_b, opt_b_img_lock, opt_b_img_wrong, opt_b_img_correct, opt_b_img_loc, opt_b_txt_rect, opt_b_char_txt_rect],
    "c": [opt_c, opt_c_img_lock, opt_c_img_wrong, opt_c_img_correct, opt_c_img_loc, opt_c_txt_rect, opt_c_char_txt_rect],
    "d": [opt_d, opt_d_img_lock, opt_d_img_wrong, opt_d_img_correct, opt_d_img_loc, opt_d_txt_rect, opt_d_char_txt_rect]
}

def check(opt, ans):
    correct_opt_char = opt_char_font.render(opt.upper() + ":", True, grey)
    correct_txt = opt_font.render(lock_data[opt][0], True, black)

    wrong_opt_char = opt_char_font.render(ans.upper() + ":", True, gold)
    wrong_txt = opt_font.render(lock_data[ans][0], True, white)

    if opt == ans:
        window.blit(lock_data[opt][3], lock_data[opt][4])
        window.blit(correct_txt, lock_data[opt][5])
        window.blit(correct_opt_char, lock_data[opt][6])
    
    else:
        window.blit(lock_data[opt][2], lock_data[opt][4])
        window.blit(lock_data[ans][3], lock_data[ans][4])
        window.blit(correct_txt, lock_data[ans][5])
        window.blit(correct_opt_char, lock_data[ans][6])
        window.blit(wrong_txt, lock_data[opt][5])
        window.blit(wrong_opt_char, lock_data[opt][6])

        pygame.mixer.Sound.play(wrong_music)

    pygame.display.update()
    pygame.time.delay(3000)

    if opt != ans:
        return False
    return True


    

def lock(opt):
    temp_opt_char = opt_char_font.render(opt.upper() + ":", True, grey)

    temp_txt = opt_font.render(lock_data[opt][0], True, black)
    window.blit(lock_data[opt][1], lock_data[opt][4])
    window.blit(temp_txt, lock_data[opt][5])
    window.blit(temp_opt_char, lock_data[opt][6])

    pygame.display.update()
    pygame.mixer.Sound.play(lock_music)
    pygame.time.delay(3000)

def game_window():
    
    pos = (0, 0)
    pygame.mixer.Sound.play(start_music)
    running = True
    while running:
        window.blit(game_bg_img, (0, 0))
        window.blit(question_img, (0, 200))
        window.blit(opt_a_img, opt_a_img_loc)
        window.blit(opt_b_img, opt_b_img_loc)
        window.blit(opt_c_img, opt_c_img_loc)
        window.blit(opt_d_img, opt_d_img_loc)

        if is_over(pos, opt_a_img_loc, opt_a_img.get_size(), 55):
            window.blit(opt_a_img_over, opt_a_img_loc)

        if is_over(pos, opt_b_img_loc, opt_b_img.get_size(), 55):
            window.blit(opt_b_img_over, opt_b_img_loc)

        if is_over(pos, opt_c_img_loc, opt_c_img.get_size(), 55):
            window.blit(opt_c_img_over, opt_c_img_loc)

        if is_over(pos, opt_d_img_loc, opt_d_img.get_size(), 55):
            window.blit(opt_d_img_over, opt_d_img_loc)

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
                exit()

            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if is_over(pos, opt_a_img_loc, opt_a_img.get_size(), 55):
                    print("Option A")
                    lock('a')
                    running = check('a', 'b')

                if is_over(pos, opt_b_img_loc, opt_b_img.get_size(), 55):
                    print("Option B")
                    lock('b')
                    running = check('b', 'b')

                if is_over(pos, opt_c_img_loc, opt_c_img.get_size(), 55):
                    print("Option C")
                    lock('c')
                    running = check('c', 'c')

                if is_over(pos, opt_d_img_loc, opt_d_img.get_size(), 55):
                    print("Option D")
                    lock('d')
                    running = check('d', 'd')
                

        pygame.display.update()


def start_window():
    pos = (0, 0)
    while True:
        window.blit(intro_img, (0, 0)) 
        window.blit(quit_img, quit_img_loc)
        window.blit(play_img, play_img_loc)

        if is_over(pos, quit_img_loc, quit_img.get_size(), 60):
            window.blit(quit_img_over, quit_img_loc)
        
        if is_over(pos, play_img_loc, play_img.get_size(), 60):
            window.blit(play_img_over, play_img_loc)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if is_over(pos, play_img_loc, play_img.get_size(), 60):
                    print("Start")
                    game_window()

                if is_over(pos, quit_img_loc, quit_img.get_size(), 60):
                    return 0

        window.blit(play_txt, play_txt_rect)
        window.blit(quit_txt, quit_txt_rect)

        pygame.display.update()


start_window()