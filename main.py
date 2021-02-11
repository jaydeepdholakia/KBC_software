import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import quiz
pygame.init()

# Declaring some variable for the program
width = 1200
height = 700
question_no = 1
difficulty = 0
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
gold = (218, 165, 32)
black = (0, 0, 0)
grey = (90, 90, 90)
money_list = ["0", "1,000", "2,000", "3,000", "5,000", "10,000", "20,000", "40,000", 
            "80,000", "160,000", "320,000", "640,000", "1,250,000", "2,500,000",
            "5,000,000", "1 Crore"]

# Setting up the Window
window = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Kaun Banega Crorepati")
icon = pygame.image.load("images/logo.png")
pygame.display.set_icon(icon)
intro_img = pygame.image.load("images/intro.jpeg")
congo_img = pygame.image.load("images/cong.jpeg")

#importing the required audio files
intro_music = pygame.mixer.Sound("audio/intro.ogg")
start_music = pygame.mixer.Sound("audio/start.ogg")
lock_music = pygame.mixer.Sound("audio/lock.ogg")
wrong_music = pygame.mixer.Sound("audio/wrong.ogg")
correct_music = pygame.mixer.Sound("audio/correct.ogg")

# importing and initialising all the images for the program
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
money_img = pygame.image.load("images/money.png")

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

quit_img_loc = (play_img.get_width(), 500)
play_img_loc = (0, 500)
opt_a_img_loc = (0, 400)
opt_b_img_loc = (600, 400)
opt_c_img_loc = (0, 500)
opt_d_img_loc = (600, 500)

# Imporing the fonts and initialising the text
intro_font = pygame.font.Font('fonts/RobotoSlab-Medium.ttf', 80)
question_font = pygame.font.Font('fonts/RobotoSlab-Medium.ttf', 30)
money_font = pygame.font.Font('fonts/RobotoSlab-Medium.ttf', 30)
opt_char_font = pygame.font.Font('fonts/RobotoSlab-SemiBold.ttf', 40)
opt_font = pygame.font.Font('fonts/RobotoSlab-Medium.ttf', 35)
rupee_font = pygame.font.Font('fonts/Indian Rupee.ttf', 30)
play_txt = intro_font.render('Play', True, white)
quit_txt = intro_font.render('Quit', True, white)
play_txt_rect = play_txt.get_rect()
quit_txt_rect = quit_txt.get_rect()
play_txt_rect.center = (300, 560)
quit_txt_rect.center = (900, 560)


# This function tell if the mouse is over any button or image
def is_over(pos, up, down, trim):
    up = (up[0]+trim, up[1])
    down = (down[0]-trim, down[1])
    if pos[0] > up[0] and pos[1] > up[1]:
        if pos[0] < up[0] + down[0] and pos[1] < up[1] + down[1]:
            return True
    else:
        return False


# This function is important
# It fetches question and update all the text accordingly
def update():
    global opt_a_char_txt, opt_b_char_txt, opt_c_char_txt, opt_d_char_txt
    global opt_a_char_txt_rect, opt_b_char_txt_rect, opt_c_char_txt_rect, opt_d_char_txt_rect
    global question, opt_a, opt_b, opt_c, opt_d, answer, opt_data, question_no, difficulty, money
    global question_txt, question_txt_1, question_txt_2, opt_a_txt, opt_b_txt, opt_c_txt, opt_d_txt, money_txt, rupee_txt
    global question_txt_rect, question_txt_1_rect, question_txt_2_rect, opt_a_txt_rect, opt_b_txt_rect
    global opt_c_txt_rect, opt_d_txt_rect, money_txt_rect, rupee_txt_rect

    # This if goes true when you hit 7 crores and it shows the congratulate screen
    if question_no == 17:
        print("Resetting")
        question_no = 1
        difficulty = 0
        window.blit(congo_img, (0, 0))
        pygame.display.update()
        pygame.mixer.Sound.play(intro_music)
        pygame.time.delay(6500)
        start_window()

    # Initialising the option character i.e A:, B:, C: and D:
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

    # Fetch questiondata accorind to difficulty store them into respective variable
    quiz_data = quiz.get_question(difficulty)
    question = quiz_data['question']
    opt_a = quiz_data['options'][0]
    opt_b = quiz_data['options'][1]
    opt_c = quiz_data['options'][2]
    opt_d = quiz_data['options'][3]
    answer = quiz_data['correct_option']
    money = money_list[question_no-1]

    print(question_no, answer, difficulty)  # print answer for easier running while testing

    # This the question wrapping logic
    if len(question) == 1:
        question_txt = question_font.render(question[0], True, white)
    else:
        question_txt_1 = question_font.render(question[0], True, white)
        question_txt_2 = question_font.render(question[1], True, white)

    # Render and initialise the money text
    opt_a_txt = opt_font.render(opt_a, True, white)
    opt_b_txt = opt_font.render(opt_b, True, white)
    opt_c_txt = opt_font.render(opt_c, True, white)
    opt_d_txt = opt_font.render(opt_d, True, white)
    money_txt = money_font.render(money, True, white)
    rupee_txt = rupee_font.render("₹", True, white)
    if question_no > 15:
        money_txt = money_font.render(money, True, gold)
        rupee_txt = rupee_font.render("₹", True, gold)
        
    # Getting the rect properies of the rendered text for positioning on the display
    if len(question) == 1:
        question_txt_rect = question_txt.get_rect()
    else:
        question_txt_1_rect = question_txt_1.get_rect()
        question_txt_2_rect = question_txt_2.get_rect()
    opt_a_txt_rect = opt_a_txt.get_rect()
    opt_b_txt_rect = opt_b_txt.get_rect()
    opt_c_txt_rect = opt_c_txt.get_rect()
    opt_d_txt_rect = opt_d_txt.get_rect()
    money_txt_rect = money_txt.get_rect()
    rupee_txt_rect = rupee_txt.get_rect()

    # Set the location of the text
    if len(question) == 1:
        question_txt_rect.center = (610, 260)
    else:
        question_txt_1_rect.center = (610, 235)
        question_txt_2_rect.center = (610, 280)
    opt_a_txt_rect.center = (150 + opt_a_txt_rect.width // 2, 435)
    opt_b_txt_rect.center = (705 + opt_b_txt_rect.width // 2, 435)
    opt_c_txt_rect.center = (150 + opt_c_txt_rect.width // 2, 540)
    opt_d_txt_rect.center = (705 + opt_d_txt_rect.width // 2, 540)
    money_txt_rect.center = (990 + money_txt_rect.width // 2, 95)
    rupee_txt_rect.center = (1000, 100)

    # this dictionalry is useful in lock and check function
    opt_data = {
        "a": [opt_a, opt_a_img_lock, opt_a_img_wrong, opt_a_img_correct, opt_a_img_loc, opt_a_txt_rect, opt_a_char_txt_rect],
        "b": [opt_b, opt_b_img_lock, opt_b_img_wrong, opt_b_img_correct, opt_b_img_loc, opt_b_txt_rect, opt_b_char_txt_rect],
        "c": [opt_c, opt_c_img_lock, opt_c_img_wrong, opt_c_img_correct, opt_c_img_loc, opt_c_txt_rect, opt_c_char_txt_rect],
        "d": [opt_d, opt_d_img_lock, opt_d_img_wrong, opt_d_img_correct, opt_d_img_loc, opt_d_txt_rect, opt_d_char_txt_rect]
    }
    
# calling update to initialise everything in the startup
update()

# This function check if your answer was correct or wrong and do stuff accordingly
def check(opt, ans):
    global question_no, difficulty

    correct_opt_char = opt_char_font.render(opt.upper() + ":", True, grey)
    correct_txt = opt_font.render(opt_data[opt][0], True, black)
    wrong_opt_char = opt_char_font.render(ans.upper() + ":", True, gold)
    wrong_txt = opt_font.render(opt_data[ans][0], True, white)

    # here if your ans matches with actual ans we call this if
    if opt == ans:
        # cheange the colour of the option to green
        window.blit(opt_data[opt][3], opt_data[opt][4])
        window.blit(correct_txt, opt_data[opt][5])
        window.blit(correct_opt_char, opt_data[opt][6])

        question_no += 1    # increase the question no
        # here increase the difficulty when reacing the thrushold
        if question_no == 6:
            difficulty = 1
        if question_no == 11:
            difficulty = 2

        # now play the correct music, update the window and wait for 1 sec
        pygame.mixer.Sound.play(correct_music)
        pygame.display.update()
        pygame.time.delay(1000)

    # this else is called when ans dont match
    else:
        # cheange the colour of your option to red and correct with green 
        window.blit(opt_data[opt][2], opt_data[opt][4])
        window.blit(opt_data[ans][3], opt_data[ans][4])
        window.blit(correct_txt, opt_data[ans][5])
        window.blit(correct_opt_char, opt_data[opt][6])
        window.blit(wrong_txt, opt_data[opt][5])
        window.blit(wrong_opt_char, opt_data[ans][6])

        # reset everyting
        question_no = 1
        difficulty = 0

        # now play the wrong music, update the window and wait for 3 sec
        pygame.mixer.Sound.play(wrong_music)
        pygame.display.update()
        pygame.time.delay(3000)

    # this returns is for game window function
    if opt != ans:
        update()
        return False
    update()
    return True


# This function is called you click on an option and that option gets locked
def lock(opt):
    # change the option color to yellow
    temp_opt_char = opt_char_font.render(opt.upper() + ":", True, grey)
    temp_txt = opt_font.render(opt_data[opt][0], True, black)
    window.blit(opt_data[opt][1], opt_data[opt][4])
    window.blit(temp_txt, opt_data[opt][5])
    window.blit(temp_opt_char, opt_data[opt][6])

    # play the lock music, update the window and wait for 3 sec
    pygame.display.update()
    pygame.mixer.Sound.play(lock_music)
    pygame.time.delay(3000)


# This is the function which whow everythin in the main game window
def game_window():
    pos = (0, 0)
    pygame.mixer.Sound.play(start_music)
    running = True
    while running:
        window.blit(game_bg_img, (0, 0))
        window.blit(question_img, (0, 200))
        window.blit(money_img, (890, 70))

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

        if len(question) == 1:
            window.blit(question_txt, question_txt_rect)
        else:
            window.blit(question_txt_1, question_txt_1_rect)
            window.blit(question_txt_2, question_txt_2_rect)

        window.blit(opt_a_txt, opt_a_txt_rect)
        window.blit(opt_b_txt, opt_b_txt_rect)
        window.blit(opt_c_txt, opt_c_txt_rect)
        window.blit(opt_d_txt, opt_d_txt_rect)
        window.blit(money_txt, money_txt_rect)
        window.blit(rupee_txt, rupee_txt_rect)

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
                    lock('a')
                    running = check('a', answer)

                if is_over(pos, opt_b_img_loc, opt_b_img.get_size(), 55):
                    lock('b')
                    running = check('b', answer)

                if is_over(pos, opt_c_img_loc, opt_c_img.get_size(), 55):
                    lock('c')
                    running = check('c', answer)

                if is_over(pos, opt_d_img_loc, opt_d_img.get_size(), 55):
                    lock('d')
                    running = check('d', answer)

        pygame.display.update()


# This the function which show the starting screen (Play, Quit)
def start_window():
    pos = (0, 0)
    update()
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
                    game_window()

                if is_over(pos, quit_img_loc, quit_img.get_size(), 60):
                    exit()

        window.blit(play_txt, play_txt_rect)
        window.blit(quit_txt, quit_txt_rect)

        pygame.display.update()

# Roll the inro in the startup 
window.blit(intro_img, (0, 0))
pygame.display.update()
pygame.mixer.Sound.play(intro_music)
pygame.time.delay(6000)

# start the game
start_window()
