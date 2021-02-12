from pytrivia import Diffculty, Type, Category, Trivia
import random
import textwrap
import pickle
import tkinter as tk
from tkinter import messagebox
import pprint

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
diffculty_list1 = ["easy", "medium", "hard"]


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

def get_funny_question(diffculty):
    with open("funny_question_data.pickle", "rb") as file:
        funny_data = pickle.load(file)

    print(diffculty_list1[diffculty])
    queston_list = funny_data[diffculty_list1[diffculty]]
    queston_data = queston_list[random.randint(0, len(queston_list)-1)]
    question = queston_data["question"]
    options = queston_data["options"]
    random.shuffle(options)
    correct_option = option_list[options.index(queston_data["correct_answer"])]
    return {'question':question, 'options': options, 'correct_option':correct_option}


def print_funny_question():
    with open("funny_question_data.pickle", "rb") as file:
        funny_data = pickle.load(file)

    for i in funny_data:
        print("\n\n" + str(i))
        for j in funny_data[i]:
            print("\n\t", j)

    messagebox.showinfo("", "Question data printed on terminal") 

def add_funny_question():
    global var
    difficulty = int(var.get() if var.get() != '' else 0)
    question = question_text.get("1.0", tk.END).rstrip()
    options = [opt1_text.get("1.0", tk.END).rstrip(), opt2_text.get("1.0", tk.END).rstrip(), 
            opt3_text.get("1.0", tk.END).rstrip(), opt4_text.get("1.0", tk.END).rstrip()]
    correct_answer = correct_opt_text.get("1.0", tk.END).rstrip()

    if not (len(question) and len(options[0]) and len(options[1]) and len(options[2]) and len(options[3]) and len(correct_answer) and difficulty):
        messagebox.showwarning("", "Please Populate all fields")
        return 0
    
    if not (len(options[0]) < 22 and len(options[1]) < 22 and len(options[2]) < 22 and len(options[3]) < 22 ):
        messagebox.showwarning("", "Options should not have more then 20 characters")
        return 0
     
    if not (len(question) < 120):
        messagebox.showwarning("", "Question should not have more then 120 characters")
        return 0
    
    if not correct_answer in options:
        messagebox.showwarning("", "The Correct Answer dosent matches any of the four options")
        return 0
        
    question_data = {'question':question, 'options': options, 'correct_answer':correct_answer}

    with open("funny_question_data.pickle", "rb") as file:
        funny_data = pickle.load(file)

    question_data = {'question':question, 'options': option_list, 'correct_answer':correct_answer}
    funny_data[diffculty_list1[difficulty-1]].append(question_data)

    with open("funny_question_data.pickle", "wb") as file:
        pickle.dump(funny_data, file, protocol=pickle.HIGHEST_PROTOCOL)

    messagebox.showinfo("", "Successfully added the funny question") 
    question_text.delete('1.0', tk.END)
    opt1_text.delete('1.0', tk.END)
    opt2_text.delete('1.0', tk.END)
    opt3_text.delete('1.0', tk.END)
    opt4_text.delete('1.0', tk.END)
    correct_opt_text.delete('1.0', tk.END)
    easy_radio.deselect()
    medium_radio.deselect()
    hard_radio.deselect()

        
if __name__ == "__main__":
    root = tk.Tk() 

    canvas = tk.Canvas(root, height=420, width=690)
    head_label = tk.Label(canvas, text='Add Funny Question', font=('verdana', 25))
    question_label = tk.Label(canvas, text='Question: ', font=('verdana', 17))
    opt1_label = tk.Label(canvas, text='Option 1: ', font=('verdana', 17))
    opt2_label = tk.Label(canvas, text='Option 2: ', font=('verdana', 17))
    opt3_label = tk.Label(canvas, text='Option 3: ', font=('verdana', 17))
    opt4_label = tk.Label(canvas, text='Option 4: ', font=('verdana', 17))
    correct_opt_label = tk.Label(canvas, text='Correct Answer: ', font=('verdana', 17))
    question_text = tk.Text(root, height=3, width=50, font=('verdana', 13))
    opt1_text = tk.Text(root, height=1, width=22, font=('verdana', 13))
    opt2_text = tk.Text(root, height=1, width=22, font=('verdana', 13))
    opt3_text = tk.Text(root, height=1, width=22, font=('verdana', 13))
    opt4_text = tk.Text(root, height=1, width=22, font=('verdana', 13))
    correct_opt_text = tk.Text(root, height=1, width=22, font=('verdana', 13))

    var = tk.StringVar()
    easy_radio = tk.Radiobutton(root, text="Easy", variable=var, value="1", font=('verdana', 17))
    medium_radio = tk.Radiobutton(root, text="Medium", variable=var, value="2", font=('verdana', 17))
    hard_radio = tk.Radiobutton(root, text="Hard", variable=var, value="3", font=('verdana', 17))
    add_button = tk.Button(canvas, text='Add New Question', font=('verdana', 15), command=add_funny_question)
    print_button = tk.Button(canvas, text='Print All Question', font=('verdana', 15), command=print_funny_question)

    canvas.pack()
    head_label.place(y=10, relx=0.25)
    question_label.place(x=3, y=85, anchor='w')
    opt1_label.place(x=3, y=125+45, anchor='w')
    opt2_label.place(x=3, y=165+45, anchor='w')
    opt3_label.place(x=3, y=205+45, anchor='w')
    opt4_label.place(x=3, y=245+45, anchor='w')
    correct_opt_label.place(x=3, y=285+45, anchor='w')
    question_text.place(x=125, y=70)
    opt1_text.place(x=125, y=125+30)
    opt2_text.place(x=125, y=165+30)
    opt3_text.place(x=125, y=205+30)
    opt4_text.place(x=125, y=245+30)
    correct_opt_text.place(x=200, y=285+30)

    easy_radio.place(x=450, y=170)
    medium_radio.place(x=450, y=210)
    hard_radio.place(x=450, y=250)

    add_button.place(x=80, y=370)
    print_button.place(x=350, y=370)

    root.mainloop()
        


