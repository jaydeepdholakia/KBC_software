from pytrivia import Diffculty, Type, Category, Trivia
import random
import time
import textwrap

# initialising the text wrapper for question
wrapper = textwrap.TextWrapper(width=60)

# initialising the trivia
my_api = Trivia(True)

category_list = [Category.Animals, Category.Sports, Category.Books,Category.Art, 
                Category.Board_Games, Category.Computers, Category.Film, Category.Maths,
                Category.Gadgets, Category.General, Category.Celebrities, Category.Nature,
                Category.History, Category.Music, Category.Mythology, Category.Tv,
                Category.Geography, Category.Politics, Category.Vehicles ]

option_list = ['a', 'b', 'c', 'd']

diffculty_list = [Diffculty.Easy, Diffculty.Medium, Diffculty.Hard]


"""
This is how the get question works, first get the difficulty from the diffculty_list 
get a random category from category_list 
now request for 5 question of that category and difficulty
Extract the list of question data from the response
now the result list has 5 queston data loop though them and if your the the questiona ans its
option of desired lenght break out of the for loop
now just return the question data
"""
# this question return the quiz data in a dictionary

def get_question(diffculty):
    global options, question
    while True:
        diffculty = diffculty_list[diffculty]
        category = category_list[random.randint(0, 18)]
        response = my_api.request(5, category, diffculty, Type.Multiple_Choice)
        response = response["results"]
        for i in range(len(response)):
            question = response[i]["question"]
            options = response[i]["incorrect_answers"]
            options.append(response[i]["correct_answer"])
            random.shuffle(options)
            correct_option = option_list[options.index(response[i]["correct_answer"])]
            question = wrapper.wrap(text=question)

            if len(options[0]) < 22 and len(options[1]) < 22 and len(options[2]) < 22 and len(options[3]) < 22 and len(question) < 3:
                return {'question':question, 'options': options, 'correct_option':correct_option}
    
        
if __name__ == "__main__":
    diffculty = 2
    for i in range(16):
        print("rum", i, diffculty)
        print(get_question(1))
        time.sleep(10)
