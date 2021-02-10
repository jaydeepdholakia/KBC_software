from pytrivia import Diffculty, Type, Category, Trivia
import random
my_api = Trivia(True)

category_list = [Category.Animals, Category.Sports, Category.Books,
Category.Art, Category.Board_Games, Category.Computers, Category.Film,
Category.Gadgets, Category.General, Category.Celebrities, Category.Maths,
Category.History, Category.Music, Category.Mythology, Category.Nature,
Category.Geography, Category.Politics, Category.Vehicles, Category.Tv]

option_list = ['a', 'b', 'c', 'd']
diffculty_list = [Diffculty.Easy, Diffculty.Medium, Diffculty.Hard]

def get_question(diffculty):
    diffculty = diffculty_list[diffculty]
    category = category_list[random.randint(0, 18)]
    response = my_api.request(1, category, diffculty, Type.Multiple_Choice)
    response = response["results"][0]
    question = response["question"]
    options = response["incorrect_answers"]
    options.append(response["correct_answer"])
    random.shuffle(options)
    correct_option = option_list[options.index(response["correct_answer"])]
    # print(response)
    return {'question':question, 'options': options, 'correct_option':correct_option}
    # return {'question':'Who painted "Swans Reflecting Elephants", "Sleep", and "The Persistence of Memory"?', 
    # 'options': ['Salvador Dali', 'Salvador Dali', 'Jackson Pollock', 'Edgar Degas'], 
    # 'correct_option':'a'}

if __name__ == "__main__":
    print(get_question(2))