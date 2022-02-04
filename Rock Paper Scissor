# import modules
from tkinter import *
import random

# define global variables
choice_list = ('Rock','Paper','Scissors')
computer_choice = ''
human_choice = ''
compare = ''
human_score = 0
computer_score = 0


# define all functions
def computerChoice():
    global choice_list, computer_choice
    computer_choice = random.choice(choice_list)
    return computer_choice
def compareChoice(computer, human):
    global compare
    if computer == human:
        compare = 'tie'
    else:
        lst = [computer,human]
        if lst == ['Rock','Paper']:
            compare = 'Win'
        elif lst == ['Paper','Rock']:
            compare = 'Lose'
        elif lst == ['Paper', 'Scissors']:
            compare = 'Win'
        elif lst == ['Scissors', 'Paper' ]:
            compare = 'Lose'
        elif lst == ['Rock','Scissors']:
            compare = 'Lose'
        else:
            compare = 'Win'

def paper():
    global human_choice
    human_choice = 'Paper'
    compareChoice( computerChoice(), human_choice )
    updateScore()
    update_show()
def rock():
    global human_choice
    human_choice = 'Rock'
    compareChoice( computerChoice(), human_choice )
    updateScore()
    update_show()
def scissors():
    global human_choice
    human_choice = 'Scissors'
    compareChoice( computerChoice(), human_choice )
    updateScore()
    update_show()
def updateScore():
    global human_score, compare
    global computer_score
    if compare == 'Win':
        human_score += 1
    else:
        computer_score += 1

def update_show():
    text_update = f'Your Choice: {human_choice}\n My Choice: {computer_choice}\n Your Score: {human_score}\n Computer Score: {computer_score}'

    text_area.config(text=text_update)


# create window
window = Tk()
window.title("Rock, Paper, Scissors - A Game for All!")
window.geometry("400x300")


# create widgets
# text
text_area = Label(text="Welcome!", bg="yellow", height=6, width=20, font=("Arial", 25))
# button
Rock = Button(window, text='Rock', fg='black', command=rock)
Paper = Button(window, text='Paper', fg='black', command=paper)
Scissors = Button(window, text='Scissors', fg='black', command=scissors)
'''text = Label(window, text='Your Choice: ')
text1 = Label(window, text='My Choice: ')
text2 = Label(window, text='Your Score: ')
text3 = Label(window, text='Computer Score: ')'''
# place widgets into window container using a layout
Rock.grid(row=0, column=0, ipadx=20)
Paper.grid(row=0, column=1, ipadx=20)
Scissors.grid(row=0, column=2, ipadx=20)
text_area.grid(row=3,column=0,rowspan=3, columnspan=3)

# open window
window.mainloop()
