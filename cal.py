from tkinter import Entry
import tkinter as tk
import random as rand
import sys
import os

root = tk.Tk()
root.geometry("450x250+500+300")
root.title("Let's play Math!")

welcomeLabel = tk.Label(text="LET'S PLAY MATH!").pack()
startLabel = tk.Label(text='Select a math operation to start').pack()

def genRandom():
    a = rand.randrange(1,10,1)
    b = rand.randrange(1,10,1)

    return a, b

def calculate(method):

    global correctAnswer

    ranNumber = genRandom()

    if method == "Add":
        correctAnswer = int(ranNumber[0] + ranNumber[1])
        calcString = "+"
    elif method == "Sub":
        correctAnswer = int(ranNumber[0] - ranNumber[1])
        calcString = "-"

    QuestionLbl = tk.Label(text="What does {0} {1} {2} equal?".format(ranNumber[0], calcString, ranNumber[1]))
    QuestionLbl.place(x=0, y=125)

    global answerEntry
    answerEntry = Entry()
    answerEntry.place(x=300, y=125)

    isCorrectBtn = tk.Button(text="Check Answer", command=isCorrect)
    isCorrectBtn.place(x=300, y = 150)
def isCorrect():

    answerEntered = int(answerEntry.get())

    if answerEntered != correctAnswer:
        checkAnswerLbl = tk.Label(text="Let's try again.")
        checkAnswerLbl.place(x=150, y=125)
    elif answerEntered == correctAnswer:
        checkAnswerLbl = tk.Label(text="Hooray!")
        checkAnswerLbl.place(x=150, y=125)

    restartBtn = tk.Button(text="Play Again?", command=playAgain)
    restartBtn.place(x=300, y = 200)

def playAgain():
    python = sys.executable
    os.execl(python, python, * sys.argv)

addBtn = tk.Button(text="Addition", command=lambda: calculate("Add"))
addBtn.place(x=160, y = 60)
subBtn = tk.Button(text="Subtraction", command=lambda: calculate("Sub"))
subBtn.place(x=220, y=60)

tk.mainloop()