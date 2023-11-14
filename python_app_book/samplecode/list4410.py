import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()


def browse():
    global dir_path
    statusbar["text"] = "Here we go!"
    dir_path = filedialog.askdirectory()


def run_func():
    try:
        for file in os.listdir(dir_path):
            if file.endswith(cb.get()):
                path = dir_path + "/" + file
                shutil.move(path, save_path)
        statusbar["text"] = "Done!"

    except:
        statusbar["text"] = "Error!"
