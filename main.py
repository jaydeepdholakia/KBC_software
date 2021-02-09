from pytrivia import Diffculty, Type, Category, Trivia
import random
from tkinter import *

root = Tk()

label1 = Label(root, text="KBC")
label2 = Label(root, text="Jaydeep Dholokia's KBC")

triv = Trivia(True)


def printOptions(res):
    ques = res["question"]
    ans = res["correct_answer"]
    opt = random.randint(0, 3)
    op = res["incorrect_answers"]
    op.insert(opt, ans)
    print(ques)
    n = 1
    for i in op:
        i = ". " + i
        print(str(n) + i)
        n = n + 1


def category():
    r = random.randint(1, 19)
    cat = ""
    if r == 1:
        cat = Category.Animals
    if r == 2:
        cat = Category.Sports
    if r == 3:
        cat = Category.Books
    if r == 4:
        cat = Category.Art
    if r == 5:
        cat = Category.Board_Games
    if r == 6:
        cat = Category.Computers
    if r == 7:
        cat = Category.Film
    if r == 8:
        cat = Category.Gadgets
    if r == 9:
        cat = Category.General
    if r == 10:
        cat = Category.Celebrities
    if r == 11:
        cat = Category.Maths
    if r == 12:
        cat = Category.History
    if r == 13:
        cat = Category.Music
    if r == 14:
        cat = Category.Mythology
    if r == 15:
        cat = Category.Nature
    if r == 16:
        cat = Category.Geography
    if r == 17:
        cat = Category.Politics
    if r == 18:
        cat = Category.Vehicles
    if r == 19:
        cat = Category.Tv

    return cat


def getQuestion(dif):
    ctgr = category()
    res = triv.request(1, ctgr, dif, Type.Multiple_Choice)
    res = res["results"][0]
    return res


q = 16
while q > 8:
    res = getQuestion(Diffculty.Easy)
    printOptions(res)
    q = q - 1
    print("\n")

while q > 4:
    res = getQuestion(Diffculty.Medium)
    printOptions(res)
    q = q - 1
    print("\n")

while q > 0:
    res = getQuestion(Diffculty.Hard)
    printOptions(res)
    q = q - 1
    print("\n")

root.mainloop()