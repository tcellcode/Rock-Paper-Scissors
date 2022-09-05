from numpy import random
from tkinter import *
from PIL import Image, ImageTk
import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))

def rock_paper_scissors(choice1, choice2):
    if choice1 == choice2: return 0.5 # tie
    beat = {
        "r" : "s",
        "p" : "r",
        "s" : "p"
    }
    return 1 if beat[choice1] == choice2 else 0

def responsive_grid(master, rows, cols):
    for i in range(rows):
        master.grid_rowconfigure(i,  weight =1)
        for j in range(cols):
            master.grid_columnconfigure(j,  weight =1)


root = Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300+500+100")
root.overrideredirect(True)


def toggle(event):
    if event.type == EventType.Map:
        root.deiconify()
    else:
        root.withdraw()

# create the "invisible" toplevel
top = Toplevel(root)
top.protocol('WM_DELETE_WINDOW', root.destroy) # close root window if toplevel is closed
top.bind("<Map>", toggle)
top.bind("<Unmap>", toggle)
top.attributes("-alpha", 0)
top.iconphoto(False, PhotoImage(file="rock-paper-scissors.png"))

# title bar
title_bar = Frame(root, bg="#6BE1A8")
title_bar.pack(fill=X)

def get_pos(event):
    xwin = event.x
    ywin = event.y

    def move_win(event):
        root.geometry(f'+{event.x_root - xwin}+{event.y_root - ywin}')
    title_bar.bind("<B1-Motion>", move_win)
    title_label.bind("<B1-Motion>", move_win)

title_bar.bind("<Button-1>", get_pos)    

# title
title_label = Label(title_bar, text="Rock Paper Scissors", font="helvetica 16 bold", bg=title_bar["bg"])
title_label.pack(side=LEFT)
title_label.bind("<Button-1>", get_pos)


# close button
close_button = Button(title_bar, command=root.destroy, text="X", font="helvetica 16 bold", fg="white", bg="red", border=0)
close_button.pack(side=RIGHT)

# minimize button
minimize_button = Button(title_bar, command=top.iconify, text="_", font="helvetica 16 bold", fg="white", bg=title_bar["bg"], border=0)
minimize_button.pack(side=RIGHT)

# main frame
main_frame = Frame(root, bg="#F1F1A6")
main_frame.pack(fill=BOTH, expand=True)
responsive_grid(main_frame, 3, 2)
# option
option = StringVar()

def sel():
    global score
    human = str(option.get())
    computer = random.choice(["rock", "paper", "scissors"])
    state = rock_paper_scissors(human, computer[0])

    txt = f"Computer choice:\n{computer}\n"
    final = {
        0 : f"{txt}You lose!",
        0.5 : f"{txt}Tie game!",
        1 : f"{txt}You win"
    }
    game_info.config(text=final[state])

rock_op = Radiobutton(main_frame, tristatevalue="x", bg=main_frame["bg"], command=sel, text="Rock", font="helvetica 16 bold", value="r", variable=option)
rock_op.grid(row=0, column=0, sticky=EW)
paper_op = Radiobutton(main_frame, tristatevalue="x", bg=main_frame["bg"], command=sel, text="Paper", font="helvetica 16 bold", value="p", variable=option)
paper_op.grid(row=1, column=0, sticky=EW)
sciss_op = Radiobutton(main_frame, tristatevalue="x", bg=main_frame["bg"], command=sel, text="Scissors", font="helvetica 16 bold", value="s", variable=option)
sciss_op.grid(row=2, column=0, sticky=EW)

# label
game_info = Label(main_frame, text="Pick one!", font="helvetica 16 bold", bg=main_frame["bg"])
game_info.grid(row=0, column=1)

render = ImageTk.PhotoImage(Image.open("rock-paper-scissors.png"))
image = Label(main_frame, image=render,)
image.grid(row=1, column=1, rowspan=2)

root.mainloop()
