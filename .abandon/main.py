import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import tkinter as tk
from PIL import Image, ImageTk

# local
import editor

root = tk.Tk()
root.geometry("700x500")
root.title("Code Editor")
root.wm_iconphoto(True, ImageTk.PhotoImage(Image.open("typing.ico")))
root.resizable(False, False)

editor_frame = tk.Frame(root, bg="#DBF9EF")
editor_frame.pack()
text_box, header = editor.frame(editor_frame)


root.mainloop()
