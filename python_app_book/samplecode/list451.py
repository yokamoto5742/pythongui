import tkinter as tk


def sub_window():
    mini_window = tk.Toplevel(root)
    mini_window.title("Mini Window")
    button2 = tk.Button(mini_window, text="push2")
    button2.pack(padx=50, pady=25)


root = tk.Tk()

button1 = tk.Button(root, text="push1", command=sub_window)
button1.pack(padx=100, pady=50)

root.mainloop()
