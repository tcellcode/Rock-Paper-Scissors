from email import header
import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
import tkinter as tk
from tkinter import Menu, filedialog
import requests, json

def save(text_box):
    try:
        # get the text from the text box
        text = text_box.get("1.0", "end-1c")
        # get the filename from the user and custom extension
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Custom Files", "*.*"), ("Text Files", ".txt")])
        # write the text to the file
        with open(filename, "w") as file:
            file.write(text)
        # tell the user the file was saved
        tk.messagebox.showinfo("Saved", "File saved successfully!")
    except:
        tk.messagebox.showerror("Error", "File could not be saved!")

def open_file(text_box):
    try:
        # get the filename from the user
        filename = filedialog.askopenfilename(filetypes=[("Custom Files", "*.*"), ("Text Files", ".txt")])
        # open the file
        with open(filename, "r") as file:
            # get the text from the file
            text = file.read()
            # deleate the text in the text box
            text_box.delete("1.0", "end-1c")
            # insert the text into the text box
            text_box.insert("1.0", text)
        # tell the user the file was opened
        tk.messagebox.showinfo("Opened", "File opened successfully!")
    except:
        tk.messagebox.showerror("Error", "File could not be opened!")

def run_code(text_box):
    pass

def configurations(text_box, file_name=None):
    try:
        file_dir = f"{os.getcwd()}\Highlight\{file_name}.json"
        with open(file_dir, "r") as file:
            text = file.read()
            text_box.delete("1.0", "end-1c")
            text_box.insert("1.0", text)
        tk.messagebox.showinfo("Opened", "File opened successfully!")
    except:
        tk.messagebox.showerror("Error", "File could not be opened!")
    

def frame(root):
    # make a header with transparent background
    header = tk.Label(root, text="Prepare For Your Interview", font=("Helvetica 20 bold"), bg="#DBF9EF")
    header.grid(column=0, row=0)
    
    option_button = tk.Menubutton(root, text="Options", font=("Helvetica 20 bold"), bg="#D4DDDA", padx=10, pady=10)
    option_button.grid(column=1, row=0)
    
    # add open file and save file options to the menu
    option_menu = tk.Menu(option_button, tearoff=0)
    option_button.config(menu=option_menu)
    option_menu.add_command(label="Open File", command=lambda: open_file(text_box), font=("Source Sans Pro", 16))
    option_menu.add_command(label="Save File", command=lambda: save(text_box), font=("Source Sans Pro", 16))
    option_menu.add_command(label="Run Code", command=lambda: run_code(text_box), font=("Source Sans Pro", 16))

    setting = Menu(option_menu, tearoff=0)
    option_menu.add_cascade(menu=setting, label="Settings", font=("Source Sans Pro", 16))
    setting.add_command(label="Code Info", command=lambda: configurations(text_box, "info"), font=("Source Sans Pro", 16))
    setting.add_command(label="Theme", command=lambda: configurations(text_box, "theme"), font=("Source Sans Pro", 16))
    
    text_box = tk.Text(root, width=50, height=20, font=("Consolas 16"), fg="black", border=0, padx=10, pady=10, tabs=30)
    text_box.grid(column=0, row=1, columnspan=2)

    return text_box, header

