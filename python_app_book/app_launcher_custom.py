import tkinter as tk
from tkinter import ttk
import subprocess
import configparser


# スタイルを設定するための関数
def configure_style():
    style = ttk.Style()
    style.theme_use('clam')  # モダンなテーマを使用

    # フレームのスタイル
    style.configure('TFrame', background='#333333')

    # ラベルフレームのスタイル
    style.configure('TLabelFrame', background='#333333', foreground='white')

    # ボタンのスタイル
    style.configure('TButton', background='#333333', foreground='white', borderwidth=1)
    style.map('TButton',
              background=[('active', '#666666')],
              foreground=[('active', 'white')])


def read_config(section):
    """指定されたセクションの設定を読み込む"""
    config = configparser.ConfigParser()
    config.read("config.ini")
    return [value for key, value in config[section].items()]


def launch_programs(section):
    """指定されたセクションのプログラムを起動する"""
    programs = read_config(section)
    for program in programs:
        subprocess.Popen(program, shell=True)


def launch_run1():
    launch_programs("Run1")


def launch_run2():
    launch_programs("Run2")


def edit_config():
    notepad = "notepad.exe"
    subprocess.run([notepad, "config.ini"])


def open_manual():
    manual_path = "manual.txt"
    subprocess.run(['start', manual_path], shell=True)


def create_ui(root):
    # スタイルを適用
    configure_style()

    frame = ttk.LabelFrame(root, text="Launcher", padding=10)
    frame.grid(row=0, column=0, padx=15, pady=15, sticky='ew')

    ttk.Button(frame, text="Run1", command=launch_run1).grid(row=0, column=0, padx=5, pady=5, sticky='ew')
    ttk.Button(frame, text="Run2", command=launch_run2).grid(row=0, column=1, padx=5, pady=5, sticky='ew')

    menubar = tk.Menu(root)
    root.configure(menu=menubar)

    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="設定", command=edit_config)
    file_menu.add_separator()
    file_menu.add_command(label="終了", command=root.destroy)

    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="マニュアル", command=open_manual)


def main():
    root = tk.Tk()
    root.title("Application Launcher")
    root.geometry('300x120')
    root.configure(bg='#333333')
    create_ui(root)
    root.mainloop()


if __name__ == "__main__":
    main()
