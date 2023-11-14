import tkinter as tk
from tkinter import ttk

root = tk.Tk()

frame = ttk.LabelFrame(root, text="Launcher", padding=10)
frame.grid(row=0, column=0, padx=15, pady=15)

run_button1 = ttk.Button(frame, text="Run1")
run_button1.grid(row=0, column=0, padx=5)

run_button2 = ttk.Button(frame, text="Run2")
run_button2.grid(row=0, column=1, padx=5)

menubar = tk.Menu(root)
root.configure(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="設定")
file_menu.add_separator()
file_menu.add_command(label="終了", command=root.destroy)

help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)

root.mainloop()
