import tkinter as tk
from tkinter import ttk

root = tk.Tk()

radio_value = tk.IntVar()

radio_1 = ttk.Radiobutton(root, text='Test1', value=1, variable=radio_value)
radio_1.grid(row=0, column=0)

radio_2 = ttk.Radiobutton(root, text='Test2', value=2, variable=radio_value)
radio_2.grid(row=1, column=0)

button = ttk.Button(root, text='Check', command=lambda: print(radio_value.get()))
button.grid(row=2, column=0)

root.mainloop()
