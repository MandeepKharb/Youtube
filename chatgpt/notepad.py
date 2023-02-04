import tkinter as tk
from tkinter import filedialog

def open_file():
    file = filedialog.askopenfile(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file:
        content = file.read()
        text.insert('1.0', content)

def save_file():
    file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file:
        content = text.get("1.0", 'end-1c')
        file.write(content)
        file.close()

root = tk.Tk()
root.title("Notepad")

text = tk.Text(root)
text.pack()

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Exit", command=root.destroy)

root.mainloop()
