import tkinter as tk
from tkinter import ttk
import subprocess
import configparser

config = configparser.ConfigParser()


def run1_func():
    config.read("config.ini")
    read_base = config["Run1"]
    app1 = read_base.get("app1")
    app2 = read_base.get("app2")

    programs = [app1, app2]
    for program in programs:
        subprocess.Popen(program)


def run2_func():
    config.read("config.ini")
    read_base = config["Run2"]
    app1 = read_base.get("app1")
    app2 = read_base.get("app2")
    app3 = read_base.get("app3")

    programs = [app1, app2, app3]
    for program in programs:
        subprocess.Popen(program)


def set_func():
    notepad = r"C:\Windows\System32\notepad.exe"
    subprocess.run([notepad, "config.ini"])


def manual_func():
    subprocess.run(["start", "manual.txt"], shell=True)


root = tk.Tk()

frame = ttk.LabelFrame(root, text="Launcher", padding=10)
frame.grid(row=0, column=0, padx=15, pady=15)

run_button1 = ttk.Button(frame, text="Run1", command=run1_func)
run_button1.grid(row=0, column=0, padx=5)

run_button2 = ttk.Button(frame, text="Run2", command=run2_func)
run_button2.grid(row=0, column=1, padx=5)

menubar = tk.Menu(root)
root.configure(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="設定", command=set_func)
file_menu.add_separator()
file_menu.add_command(label="終了", command=root.destroy)

help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="マニュアル", command=manual_func)

root.mainloop()
