import tkinter as tk
from tkinter import ttk, filedialog
import os
import shutil


def browse():
    global dir_path
    statusbar["text"] = "Here we go!"
    dir_path = filedialog.askdirectory()


def run_func():
    try:
        save_path = filedialog.askdirectory()
        for file in os.listdir(dir_path):
            if file.endswith(cb.get()):
                path = dir_path + "/" + file
                shutil.move(path, save_path)
        statusbar["text"] = "Done!"

    except:
        statusbar["text"] = "Error!"


root = tk.Tk()

statusbar = tk.Label(root, text="Here we go!!", bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar.pack(side=tk.BOTTOM, fill=tk.X)

run_button = tk.Button(root, text="移動先フォルダ選択", command=run_func)
run_button.pack(side=tk.BOTTOM, padx=20, pady=10)

frame = ttk.LabelFrame(root, text="拡張子の選択",
                       padding=10)
frame.pack(padx=20, pady=5, side=tk.BOTTOM)

extensions = [".docx", ".txt", ".py", ".xlsx", ".zip"]
cb = ttk.Combobox(frame, values=extensions, state="readonly")
cb.pack(side=tk.LEFT)
cb.current(0)

browse_button = tk.Button(frame, text="フォルダ選択", command=browse)
browse_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
